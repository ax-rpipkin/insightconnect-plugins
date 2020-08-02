# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get alert data by ID"


class Input:
    ALERT_ID = "alert_id"
    

class Output:
    ALERT = "alert"
    

class GetAlertInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "alert_id": {
      "type": "string",
      "title": "Alert ID",
      "description": "Alert ID e.g. 597b8c751c7ff17fcf028e54",
      "order": 1
    }
  },
  "required": [
    "alert_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAlertOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "alert": {
      "$ref": "#/definitions/alert",
      "title": "Alert",
      "description": "Detailed alert data",
      "order": 1
    }
  },
  "required": [
    "alert"
  ],
  "definitions": {
    "alert": {
      "type": "object",
      "title": "alert",
      "properties": {
        "agentId": {
          "type": "string",
          "title": "Agent ID",
          "description": "ID of the agent that generated the alert",
          "order": 11
        },
        "createdAt": {
          "type": "string",
          "title": "Created At",
          "description": "Date and time the alert was fired",
          "order": 4
        },
        "datasource": {
          "type": "string",
          "title": "Datasource",
          "description": "Indicates whether this alert was generated from a CloudTrail event or Agent event. Agent events will have AgentId",
          "order": 3
        },
        "dismissReason": {
          "type": "string",
          "title": "Dismiss Reason",
          "description": "Either BUSINESS_OP, COMPANY_POLICY, MAINTENANCE, NONE, AUTO_DISMISS, or OTHER",
          "order": 7
        },
        "dismissReasonText": {
          "type": "string",
          "title": "Dismiss Reason Text",
          "description": "Reason the alert was dismissed if dismiss reason is OTHER",
          "order": 8
        },
        "dismissedAt": {
          "type": "string",
          "title": "Dismissed At",
          "description": "Date and time the alert was dismissed",
          "order": 6
        },
        "dismissedBy": {
          "type": "string",
          "title": "Dismissed By",
          "description": "Person that dismissed the alert",
          "order": 9
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID of the alert",
          "order": 1
        },
        "isDismissed": {
          "type": "boolean",
          "title": "Is Dismissed",
          "description": "Flag that shows if the alert was dismissed",
          "order": 5
        },
        "ruleId": {
          "type": "string",
          "title": "Rule ID",
          "description": "ID of the rule that generated the alert",
          "order": 12
        },
        "rulesetId": {
          "type": "string",
          "title": "Ruleset ID",
          "description": "ID of the ruleset that generated the alert",
          "order": 13
        },
        "severity": {
          "type": "number",
          "title": "Severity",
          "description": "Severity of the alert. Either 1, 2, or 3",
          "order": 10
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Title of the alert",
          "order": 2
        }
      },
      "required": [
        "severity"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)