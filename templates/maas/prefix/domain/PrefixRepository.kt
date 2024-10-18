package cl.bci.mach.product.qrbip.prefix.domain

import cl.bci.mach.libraries.network.responses.ApiResponse
import cl.bci.mach.product.qrbip.prefix.data.model.RemoteGetPrefixDataResponse
import kotlinx.coroutines.flow.Flow

interface PrefixRepository {
    suspend fun getPrefixData(): Flow<ApiResponse<RemoteGetPrefixDataResponse>>
}