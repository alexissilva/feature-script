package cl.bci.mach.product.qrbip.prefix.presentation.prefix

import cl.bci.sismo.mach.core.mvi.events.MviEffect
import cl.bci.sismo.mach.core.mvi.events.MviResult
import cl.bci.sismo.mach.core.mvi.events.MviUiState
import cl.bci.sismo.mach.core.mvi.events.MviUserIntent

sealed class PrefixUserIntent : MviUserIntent {
    object ClickIntent : PrefixUserIntent()
}

sealed class PrefixUiState : MviUiState {
    object DefaultUiState : PrefixUiState()
    object LoadingUiState : PrefixUiState()
    object SuccessUiState : PrefixUiState()
    object ErrorUiState : PrefixUiState()
}

sealed class PrefixEffect : MviEffect {
    object ShowToastEffect : PrefixEffect()
}

sealed class PrefixResult : MviResult {
    object LoadingResult : PrefixResult()
    object SuccessResult : PrefixResult()
    object ErrorResult : PrefixResult()
}