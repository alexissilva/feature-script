package cl.bci.mach.product.qrbip.prefix.data

import cl.bci.mach.product.qrbip.prefix.data.source.PrefixRemote
import cl.bci.mach.product.qrbip.prefix.domain.PrefixRepository
import javax.inject.Inject

class PrefixRepositoryImpl @Inject constructor(
    private val remote: PrefixRemote,
) : PrefixRepository {
    override suspend fun getPrefixData() = remote.getPrefixData()

}