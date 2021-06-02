# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Sends a request to the specified endpoint to perform or configure a scan"


class Input:
    AGENT = "agent"
    

class Output:
    ID = "id"
    REQUESTED_AT = "requested_at"
    STATUS = "status"
    

class AntivirusScanInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent": {
      "type": "string",
      "title": "Agent",
      "description": "Agent ID, IPv4 address, IPv6 address, MAC address or hostname",
      "order": 1
    }
  },
  "required": [
    "agent"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AntivirusScanOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "ID",
      "description": "Antivirus scan ID",
      "order": 1
    },
    "requested_at": {
      "type": "string",
      "title": "Requested At",
      "description": "Antivirus scan requested at",
      "order": 3
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Antivirus scan status",
      "order": 2
    }
  },
  "required": [
    "id",
    "requested_at",
    "status"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)