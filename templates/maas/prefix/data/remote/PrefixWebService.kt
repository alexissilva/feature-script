package cl.bci.mach.product.qrbip.prefix.data.remote

import cl.bci.mach.libraries.network.responses.ApiResponse
import cl.bci.mach.product.qrbip.prefix.data.model.RemoteGetPrefixDataResponse
import retrofit2.http.GET

interface PrefixWebService {
    @GET("prefix-url")
    suspend fun getPrefixData(): ApiResponse<RemoteGetPrefixDataResponse>
}