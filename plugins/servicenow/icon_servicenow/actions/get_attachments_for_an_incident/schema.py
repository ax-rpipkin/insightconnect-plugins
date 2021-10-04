# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Search for attachments for a given incident ID"


class Input:
    INCIDENT_ID = "incident_id"
    

class Output:
    INCIDENT_ATTACHMENTS = "incident_attachments"
    

class GetAttachmentsForAnIncidentInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "incident_id": {
      "type": "string",
      "title": "Incident ID",
      "description": "ID of the incident",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAttachmentsForAnIncidentOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "incident_attachments": {
      "type": "array",
      "title": "Incident Attachments",
      "description": "Attachments for a given incident ID",
      "items": {
        "type": "string",
        "displayType": "bytes",
        "format": "bytes"
      },
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
