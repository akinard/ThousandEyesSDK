# AlertObj


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_start** | **datetime** | reflects the date that the source began reporting a measurement that exceeded the alert rule’s threshold, expressed in UTC | [optional] 
**date_end** | **datetime** | reflects the earlier of the date that the alert was cleared, or the source reported a measurement that was under the alert rule’s threshold, expressed in UTC | [optional] 
**active** | **bool** | if the particular source is alerting when the API is queried, this flag will be set to 1. After an alert has cleared, this flag (regardless of the source’s metrics) will be set to 0, even if the particular source has not cleared the alert rule. | [optional] 
**metrics_at_start** | **str** | string representation of the metric at the time that the source began alerting. Note that the alert start and dateStart for a particular source do not need to be the same, as sources may change alerting status throughout an alert’s lifecycle | [optional] 
**metrics_at_end** | **str** | string representation of the metric or metrics being considered in the alert rule at the point that the alert was cleared. If the alert is not yet cleared, this field reflects the last round of data gathered from the source. | [optional] 
**permalink** | **str** | hyperlink to alerts list, with row expanded | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


