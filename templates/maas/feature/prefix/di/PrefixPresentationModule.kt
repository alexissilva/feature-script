package cl.bci.mach.product.qrbip.prefix.di

import androidx.lifecycle.ViewModel
import cl.bci.mach.product.qrbip.onboarding.presentation.OnboardingViewModel
import cl.bci.mach.product.qrbip.prefix.presentation.PrefixViewModel
import cl.bci.sismo.mach.maas.core.di.ViewModelKey
import dagger.Binds
import dagger.Module
import dagger.multibindings.IntoMap


@Module
internal abstract class PrefixPresentationModule {

    @Binds
    @IntoMap
    @ViewModelKey(PrefixViewModel::class)
    abstract fun bindPrefixViewModel(viewModel: PrefixViewModel): ViewModel

}