package cl.bci.mach.product.qrbip.prefix.presentation.prefix

import cl.bci.mach.libraries.network.responses.suspendOnError
import cl.bci.mach.libraries.network.responses.suspendOnException
import cl.bci.mach.libraries.network.responses.suspendOnSuccess
import cl.bci.mach.libraries.utils.log.SdkLog
import cl.bci.mach.product.qrbip.prefix.domain.PrefixRepository
import cl.bci.mach.product.qrbip.prefix.presentation.prefix.PrefixEffect.ShowToastEffect
import cl.bci.mach.product.qrbip.prefix.presentation.prefix.PrefixResult.ErrorResult
import cl.bci.mach.product.qrbip.prefix.presentation.prefix.PrefixResult.LoadingResult
import cl.bci.mach.product.qrbip.prefix.presentation.prefix.PrefixResult.SuccessResult
import cl.bci.mach.product.qrbip.prefix.presentation.prefix.PrefixUserIntent.ClickIntent
import cl.bci.sismo.mach.core.mvi.execution.flow.ExecutionThread
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.FlowCollector
import kotlinx.coroutines.flow.flow
import kotlinx.coroutines.flow.flowOn
import kotlinx.coroutines.flow.onStart
import javax.inject.Inject

class PrefixProcessor @Inject constructor(
    private val repository: PrefixRepository,
    private val executionThread: ExecutionThread,
) {
    internal fun process(
        intent: PrefixUserIntent,
        emitEffect: suspend (PrefixEffect) -> Unit,
    ): Flow<PrefixResult> = when (intent) {
        is ClickIntent -> getPrefixData(emitEffect)
    }

    private fun getPrefixData(
        emitEffect: suspend (PrefixEffect) -> Unit,
    ): Flow<PrefixResult> = flow {
        repository.getPrefixData().collect { response ->
            response
                .suspendOnSuccess {
                    //emit(SuccessResult)
                    SdkLog.d(TAG, "getPrefixData success")
                }
                .suspendOnError {
                    //emit(ErrorResult)
                    SdkLog.d(TAG, "getPrefixData error")

                }
                .suspendOnException {
                    //emit(ErrorResult)
                    SdkLog.d(TAG, "getPrefixData exception")

                }
            emitPrefixResultsForDemoTest()
            emitEffect(ShowToastEffect)
        }
    }.onStart {
        emit(LoadingResult)
    }.flowOn(executionThread.ioThread())


    private suspend fun FlowCollector<PrefixResult>.emitPrefixResultsForDemoTest() {
        emit(LoadingResult)
        delay(1000)
        emit(ErrorResult)
        delay(1000)
        emit(LoadingResult)
        delay(1000)
        emit(SuccessResult)
    }

    companion object {
        private const val TAG = "PrefixProcessor"
    }
}