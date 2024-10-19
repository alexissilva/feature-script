package cl.bci.mach.product.qrbip.prefix.navigation

import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavGraphBuilder
import androidx.navigation.compose.composable
import androidx.navigation.navigation
import cl.bci.mach.product.qrbip.prefix.ui.PrefixScreen

const val PREFIX_NAVIGATION_ROUTE = "prefixNavigation"
const val PREFIX_SCREEN_ROUTE = "prefixScreen"

fun NavGraphBuilder.prefixNavigation(
    factory: ViewModelProvider.Factory
) {
    navigation(
        route = PREFIX_NAVIGATION_ROUTE,
        startDestination = PREFIX_SCREEN_ROUTE,
    ) {
        prefixScreen(factory)
    }
}

private fun NavGraphBuilder.prefixScreen(factory: ViewModelProvider.Factory) {
    composable(PREFIX_SCREEN_ROUTE) {
        PrefixScreen(
            viewModel = viewModel(factory = factory)
        )
    }
}