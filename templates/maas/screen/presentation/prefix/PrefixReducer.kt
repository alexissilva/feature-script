package cl.bci.mach.product.qrbip.feature.presentation.prefix

import cl.bci.mach.product.qrbip.feature.presentation.prefix.PrefixResult.ErrorResult
import cl.bci.mach.product.qrbip.feature.presentation.prefix.PrefixResult.LoadingResult
import cl.bci.mach.product.qrbip.feature.presentation.prefix.PrefixResult.SuccessResult
import cl.bci.mach.product.qrbip.feature.presentation.prefix.PrefixUiState.ErrorUiState
import cl.bci.mach.product.qrbip.feature.presentation.prefix.PrefixUiState.LoadingUiState
import cl.bci.mach.product.qrbip.feature.presentation.prefix.PrefixUiState.SuccessUiState
import cl.bci.sismo.mach.core.mvi.MviReducer
import javax.inject.Inject


class PrefixReducer @Inject constructor() : MviReducer<PrefixUiState, PrefixResult> {
    override fun PrefixUiState.reduce(result: PrefixResult): PrefixUiState =
        reduceIgnoringCurrentState(result)


    private fun reduceIgnoringCurrentState(result: PrefixResult): PrefixUiState =
        when (result) {
            ErrorResult -> ErrorUiState
            LoadingResult -> LoadingUiState
            SuccessResult -> SuccessUiState
        }


}