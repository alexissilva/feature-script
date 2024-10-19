package cl.bci.mach.product.qrbip.feature.presentation.prefix

import cl.bci.mach.product.qrbip.feature.presentation.prefix.PrefixEffect.ShowToastEffect
import cl.bci.mach.product.qrbip.feature.presentation.prefix.PrefixResult.ErrorResult
import cl.bci.mach.product.qrbip.feature.presentation.prefix.PrefixResult.LoadingResult
import cl.bci.mach.product.qrbip.feature.presentation.prefix.PrefixResult.SuccessResult
import cl.bci.mach.product.qrbip.feature.presentation.prefix.PrefixUserIntent.ClickIntent
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.flow
import javax.inject.Inject

class PrefixProcessor @Inject constructor() {
    internal fun process(
        intent: PrefixUserIntent,
        emitEffect: suspend (PrefixEffect) -> Unit,
    ): Flow<PrefixResult> = when (intent) {
        is ClickIntent -> simulateEndpointCall(emitEffect)
    }

    private fun simulateEndpointCall(
        emitEffect: suspend (PrefixEffect) -> Unit,
    ): Flow<PrefixResult> = flow {
        val results = listOf(LoadingResult, ErrorResult, LoadingResult, SuccessResult)
        for (result in results) {
            delay(1000)
            emit(result)
        }
        emitEffect(ShowToastEffect)
    }
}
