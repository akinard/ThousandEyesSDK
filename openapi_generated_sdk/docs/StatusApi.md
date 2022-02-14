# openapi_client.StatusApi

All URIs are relative to *https://api.thousandeyes.com/v6*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status_get**](StatusApi.md#status_get) | **GET** /status | This returns the current controller time (in epoch format)


# **status_get**
> InlineResponse200 status_get()

This returns the current controller time (in epoch format)

This is simply intended for verification that the API is currently running.

### Example


```python
import time
import openapi_client
from openapi_client.api import status_api
from openapi_client.model.inline_response200 import InlineResponse200
from pprint import pprint
# Defining the host is optional and defaults to https://api.thousandeyes.com/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.thousandeyes.com/v6"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = status_api.StatusApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # This returns the current controller time (in epoch format)
        api_response = api_instance.status_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StatusApi->status_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | current controller time (in epoch format) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

