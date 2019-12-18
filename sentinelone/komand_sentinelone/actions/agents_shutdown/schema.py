# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Sends a shutdown command to all agents matching the input filter"


class Input:
    FILTER = "filter"
    

class Output:
    AFFECTED = "affected"
    

class AgentsShutdownInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "filter": {
      "type": "object",
      "title": "Filter JSON",
      "description": "Applied filter - only matched agents will be affected by the requested action. Note - one of the following filter arguments must be supplied - ids, groupIds, filterId",
      "order": 1
    }
  },
  "required": [
    "filter"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AgentsShutdownOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "affected": {
      "type": "integer",
      "title": "Affected",
      "description": "Number of entities affected by the requested operation",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)