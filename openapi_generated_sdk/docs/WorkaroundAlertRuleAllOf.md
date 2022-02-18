# WorkaroundAlertRuleAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_name** | **str** | name of the alert rule | 
**expression** | **str** | string expression of alert rule | 
**alert_type** | **str** | type of alert rule, as determined by metric selection | 
**rounds_violating_out_of** | **int** | specifies the divisor (y value) for the “X of Y times” condition. | 
**rule_id** | **int** | unique ID of the alert rule | [optional] 
**direction** | **str** | optional field with one of the following values: &#x60;TO_TARGET&#x60;, &#x60;FROM_TARGET&#x60;, &#x60;BIDIRECTIONAL&#x60;, for applicable alert types (eg. path trace, End-to-End (Agent) etc.) | [optional] 
**notify_on_clear** | **bool** | 1 to send notification when alert clears | [optional] 
**default** | **bool** | Alert rules allow up to 1 alert rule to be selected as a default for each type. By checking the default option, this alert rule will be automatically included on subsequently created tests that test a metric used in alerting here | [optional] 
**minimum_sources** | **int** | the minimum number of agents or monitors that must meet the specified criteria in order to trigger the alert | [optional] 
**minimum_sources_pct** | **int** | the minimum percentage of all assigned agents or monitors that must meet the specified criteria in order to trigger the alert | [optional] 
**rounds_violationg_mode** | **str** | &#x60;EXACT&#x60; requires that the same agent(s) meet the threshold in consecutive rounds; default is &#x60;ANY&#x60; | [optional] 
**rounds_violation_required** | **int** | specifies the numerator (x value) for the “X of Y times” condition | [optional] 
**test_ids** | **[int]** |  | [optional] 
**include_covered_prefixes** | **bool** | set to 1 to include covered prefixes in the BGP alert rule. Only applicable to BGP alert rules | [optional] 
**notifications** | [**[AlertRuleNotifications]**](AlertRuleNotifications.md) | Alert notification object | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


