# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Comment on an issue"


class Input:
    COMMENT = "comment"
    ID = "id"
    

class Output:
    COMMENT_ID = "comment_id"
    

class CommentIssueInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "comment": {
      "type": "string",
      "title": "Comment",
      "description": "Comment to add",
      "order": 2
    },
    "id": {
      "type": "string",
      "title": "ID",
      "description": "Issue ID",
      "order": 1
    }
  },
  "required": [
    "comment",
    "id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CommentIssueOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "comment_id": {
      "type": "string",
      "title": "Comment ID",
      "description": "Comment ID",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)