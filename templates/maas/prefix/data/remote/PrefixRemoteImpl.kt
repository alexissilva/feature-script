package cl.bci.mach.product.qrbip.prefix.data.remote

import cl.bci.mach.libraries.utils.flowOf
import cl.bci.mach.product.qrbip.prefix.data.source.PrefixRemote
import javax.inject.Inject

class PrefixRemoteImpl @Inject constructor(
    private val api: PrefixWebService,
) : PrefixRemote {

    override fun getPrefixData() = flowOf { api.getPrefixData() }

}