# Alert


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id** | **int** | unique ID of the alert; each alert occurrence is assigned a new unique ID | [optional] 
**test_id** | **int** | unique ID of the test (see &#x60;/tests/{testId}&#x60; endpoint for more detail) | [optional] 
**rule_id** | **int** | unique ID of the alert rule (see &#x60;/alert-rules&#x60; endpoint for more detail) | [optional] 
**test_name** | **str** | name of the test | [optional] 
**active** | **int** | 0 for inactive, 1 for active, 2 for disabled. Alert is disabled if either alert rule itself has been deleted or the test it is applied to has been disabled, deleted, disabled alerting, or disassociated the alert rule from the test | [optional] 
**rule_expression** | **str** | string expression of alert rule | [optional] 
**date_start** | **datetime** | the date/time where an alert rule was triggered, expressed in UTC | [optional] 
**date_end** | **datetime** | the date/time where the alert was marked as cleared, expressed in UTC | [optional] 
**violation_count** | **int** | number of sources currently meeting the alert criteria | [optional] 
**rule_name** | **str** | name of the alert rule | [optional] 
**permalink** | **str** | hyperlink to alerts list, with row expanded | [optional] 
**type** | **str** | type of alert being triggered | [optional] 
**agents** | [**[AlertAgentObj]**](AlertAgentObj.md) | array of agents where the alert has at some point been active since the point that the alert was triggered. Not shown on BGP alerts. | [optional] 
**monitors** | [**[AlertMonitorObj]**](AlertMonitorObj.md) | array of agents where the alert has at some point been active since the point that the alert was triggered. Not shown on BGP alerts. | [optional] 
**api_links** | [**[AlertApiLinks]**](AlertApiLinks.md) | list of hyperlinks to other areas of the API | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


