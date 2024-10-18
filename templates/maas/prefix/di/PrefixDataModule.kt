package cl.bci.mach.product.qrbip.prefix.di

import ExtendedWebServiceCreator
import cl.bci.mach.product.qrbip.prefix.data.source.PrefixRemote
import cl.bci.mach.product.qrbip.prefix.data.PrefixRepositoryImpl
import cl.bci.mach.product.qrbip.prefix.data.remote.PrefixWebService
import cl.bci.mach.libraries.network.config.NetworkDependencies
import cl.bci.mach.libraries.network.config.VariantUrls
import cl.bci.mach.libraries.network.retrofit.WebServiceFactory
import cl.bci.mach.product.qrbip.prefix.data.remote.PrefixRemoteImpl
import cl.bci.mach.product.qrbip.prefix.domain.PrefixRepository
import dagger.Binds
import dagger.Module
import dagger.Provides

@Module
internal abstract class PrefixDataModule {

    @Binds
    abstract fun bindRepository(repository: PrefixRepositoryImpl): PrefixRepository

    @Binds
    abstract fun bindRemote(remote: PrefixRemoteImpl): PrefixRemote


    companion object {
        @Provides
        @JvmStatic
        fun providePrefixWebService(
            dependencies: NetworkDependencies,
            variantUrls: VariantUrls,
        ): PrefixWebService = WebServiceFactory(
            tClass = PrefixWebService::class.java,
            isDebug = dependencies.isDebug,
            interceptorParams = dependencies.interceptorParams,
            variantUrls = variantUrls,
            webServiceCreator = ExtendedWebServiceCreator(
                PrefixWebService::class.java,
                dependencies.context,
            )
        ).createWebServiceInstance(dependencies.flavorName)
    }
}