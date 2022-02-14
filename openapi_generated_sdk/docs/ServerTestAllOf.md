# ServerTestAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents** | [**[ServerTestAllOfAgents]**](ServerTestAllOfAgents.md) | array of agent objects &#x60;{\&quot;agentId\&quot;: agentId}&#x60;; get agentId from /agents endpoint. | [optional] 
**bandwidth_measurements** | **bool** | set to 1 to measure bandwidth. Only applies to Enterprise Agents assigned to the test, and requires that networkMeasurements is set. | [optional] 
**bgp_measurements** | **bool** | choose 1 to enable bgp measurements, 0 to disable; defaults to 1 when networkMeasurements is set | [optional] 
**bgp_monitors** | [**[ServerTestAllOfBgpMonitors]**](ServerTestAllOfBgpMonitors.md) | array of BGP Monitor objects &#x60;{\&quot;monitorId\&quot;: monitorId}&#x60;; get monitorId from /bgp-monitors endpoint. | [optional] 
**interval** | [**TestInterval**](TestInterval.md) |  | [optional] 
**mtu_measurements** | **bool** | set to 1 to measure MTU sizes on network from agents to the target | [optional] 
**network_measurements** | **bool** | choose 1 to enable network measurements, 0 to disable; defaults to 1 | [optional] 
**num_path_traces** | **int** | defaults to 3 | [optional] 
**path_trace_mode** | **str** | choose &#x60;inSession&#x60; to perform the path trace within a TCP session; defaults to &#x60;classic&#x60; | [optional] 
**probe_mode** | **str** | probe mode used by End-to-end Network Test; only valid if &#x60;protocol&#x60; is set to &#x60;TCP&#x60;; defaults to &#x60;AUTO&#x60; | [optional] 
**protocol** | **str** | protocol used by dependent Network tests (End-to-end, Path Trace, PMTUD); defaults to &#x60;TCP&#x60; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


