package cl.bci.mach.product.qrbip.prefix.ui

import android.widget.Toast
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.tooling.preview.Preview
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import cl.bci.mach.libraries.design.ui.atom.SpacerL
import cl.bci.mach.libraries.design.ui.atom.SpacerS
import cl.bci.mach.libraries.design.ui.atom.Text
import cl.bci.mach.libraries.design.ui.molecule.button.Button
import cl.bci.mach.libraries.design.ui.theme.M2BTheme
import cl.bci.mach.product.qrbip.prefix.presentation.PrefixViewModel
import cl.bci.mach.product.qrbip.prefix.presentation.prefix.PrefixEffect.ShowToastEffect
import cl.bci.mach.product.qrbip.prefix.presentation.prefix.PrefixUiState
import kotlinx.coroutines.launch

@Composable
fun PrefixScreen(
    viewModel: PrefixViewModel,
) {
    val scope = rememberCoroutineScope()
    val uiState by remember { viewModel.uiStates() }.collectAsStateWithLifecycle()
    val uiEffect by remember { viewModel.uiEffect() }.collectAsState(null)

    LaunchedEffect(Unit) {
        viewModel.startProcessingUserIntents()
    }

    val context = LocalContext.current
    LaunchedEffect(uiEffect) {
        when (uiEffect) {
            ShowToastEffect -> Toast.makeText(context, "Prefix Toast", Toast.LENGTH_SHORT).show();
            null -> {}
        }
    }

    PrefixScreenTemplate(
        uiState = uiState,
        onClick = { scope.launch { viewModel.emitOnClickIntent() } },
    )
}

@Preview(showBackground = true)
@Composable
fun PrefixScreenTemplate(
    uiState: PrefixUiState? = null,
    onClick: () -> Unit = {}
) {
    val stateName = uiState?.javaClass?.simpleName
    Box(
        modifier = Modifier.fillMaxSize(),
        contentAlignment = Alignment.Center
    ) {
        Column(horizontalAlignment = Alignment.CenterHorizontally) {
            Text(text = "PrefixScreen", style = M2BTheme.typography.subHeadlineM)
            SpacerS()
            Text(text = "State $stateName", style = M2BTheme.typography.bodyL)
            SpacerL()
            Button(text = "Get prefix data") { onClick() }
        }
    }
}