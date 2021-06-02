# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "This action is used to increment a counter"


class Input:
    COUNT = "count"
    RATE = "rate"
    STAT = "stat"
    

class Output:
    INCREMENT = "increment"
    STAT = "stat"
    

class IncrInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "count": {
      "type": "integer",
      "title": "Increment amount",
      "description": "The amount to increment by e.g. 1. Default is 1",
      "order": 2
    },
    "rate": {
      "type": "number",
      "title": "Sample rate",
      "description": "A sample rate e.g. 1. Default is 1",
      "order": 3
    },
    "stat": {
      "type": "string",
      "title": "Counter name",
      "description": "The name of the counter to increment",
      "order": 1
    }
  },
  "required": [
    "stat"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class IncrOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "increment": {
      "type": "integer",
      "title": "Increment",
      "description": "The number incremented by",
      "order": 2
    },
    "stat": {
      "type": "string",
      "title": "Stat",
      "description": "The name of the incremented counter",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)