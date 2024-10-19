package cl.bci.mach.product.qrbip.feature.presentation

import cl.bci.mach.product.qrbip.feature.presentation.prefix.PrefixReducer
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import cl.bci.mach.product.qrbip.feature.presentation.prefix.PrefixEffect
import cl.bci.mach.product.qrbip.feature.presentation.prefix.PrefixProcessor
import cl.bci.mach.product.qrbip.feature.presentation.prefix.PrefixResult
import cl.bci.mach.product.qrbip.feature.presentation.prefix.PrefixUiState
import cl.bci.mach.product.qrbip.feature.presentation.prefix.PrefixUiState.DefaultUiState
import cl.bci.mach.product.qrbip.feature.presentation.prefix.PrefixUserIntent
import cl.bci.sismo.mach.core.mvi.flow.MviPresentation
import cl.bci.sismo.mach.core.mvi.flow.MviPresentationEffect
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.MutableSharedFlow
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.buffer
import kotlinx.coroutines.flow.flatMapMerge
import kotlinx.coroutines.flow.launchIn
import kotlinx.coroutines.flow.onEach
import kotlinx.coroutines.flow.scan
import javax.inject.Inject


class PrefixViewModel @Inject constructor(
    private val processor: PrefixProcessor,
    private val reducer: PrefixReducer
) : ViewModel(),
    MviPresentation<PrefixUserIntent, PrefixUiState>,
    MviPresentationEffect<PrefixEffect> {

    private val defaultUiState: PrefixUiState = DefaultUiState
    private val uiState = MutableStateFlow(defaultUiState)
    private val userIntents = MutableSharedFlow<PrefixUserIntent>()
    private val uiEffect = MutableSharedFlow<PrefixEffect>()

    override fun processUserIntents(userIntents: Flow<PrefixUserIntent>) {
        userIntents
            .buffer()
            .processIntent()
            .reduceResult()
            .saveState()
            .launchIn(viewModelScope)
    }

    private fun Flow<PrefixUserIntent>.processIntent(): Flow<PrefixResult> =
        flatMapMerge { userIntent ->
            processor.process(
                intent = userIntent,
                emitEffect = { effect -> uiEffect.emit(effect) }
            )
        }

    private fun Flow<PrefixResult>.reduceResult(): Flow<PrefixUiState> =
        scan(defaultUiState) { currentUiState, result ->
            with(reducer) { currentUiState reduce result }
        }

    private fun Flow<PrefixUiState>.saveState(): Flow<PrefixUiState> =
        onEach { newState -> uiState.emit(newState) }


    override fun uiStates() = uiState
    override fun uiEffect() = uiEffect

    fun startProcessingUserIntents() {
        processUserIntents(userIntents)
    }

    suspend fun emitOnClickIntent() {
        userIntents.emit(PrefixUserIntent.ClickIntent)
    }

}
