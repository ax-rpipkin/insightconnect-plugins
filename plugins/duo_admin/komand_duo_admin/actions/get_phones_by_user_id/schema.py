# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Gets a list of phones associated with the user ID"


class Input:
    USER_ID = "user_id"
    

class Output:
    PHONE_LIST = "phone_list"
    

class GetPhonesByUserIdInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "user_id": {
      "type": "string",
      "title": "User ID",
      "description": "User ID, e.g. DUCUULF6HBMZ43IG9MBH",
      "order": 1
    }
  },
  "required": [
    "user_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetPhonesByUserIdOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "phone_list": {
      "type": "array",
      "title": "Phone List",
      "description": "List of phones associated with the user's ID",
      "items": {
        "$ref": "#/definitions/phone_user"
      },
      "order": 1
    }
  },
  "definitions": {
    "phone_user": {
      "type": "object",
      "title": "phone_user",
      "properties": {
        "activated": {
          "type": "boolean",
          "title": "Activated",
          "description": "Activated",
          "order": 1
        },
        "capabilities": {
          "type": "array",
          "title": "Capabilities",
          "description": "Capabilities",
          "items": {
            "type": "string"
          },
          "order": 2
        },
        "extension": {
          "type": "string",
          "title": "Extension",
          "description": "Extension",
          "order": 3
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 4
        },
        "number": {
          "type": "string",
          "title": "Number",
          "description": "Number",
          "order": 5
        },
        "phone_id": {
          "type": "string",
          "title": "Phone ID",
          "description": "Phone ID",
          "order": 6
        },
        "platform": {
          "type": "string",
          "title": "Platform",
          "description": "Platform",
          "order": 7
        },
        "postdelay": {
          "type": "string",
          "title": "Post delay",
          "description": "Post delay",
          "order": 8
        },
        "predelay": {
          "type": "string",
          "title": "Predelay",
          "description": "Predelay",
          "order": 9
        },
        "sms_passcodes_sent": {
          "type": "boolean",
          "title": "SMS Passcodes Sent",
          "description": "SMS passcodes sent",
          "order": 10
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 11
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)