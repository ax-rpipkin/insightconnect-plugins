# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    CRED_TOKEN = "cred_token"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "cred_token": {
      "$ref": "#/definitions/credential_token",
      "title": "API Token",
      "description": "API Token",
      "order": 1
    }
  },
  "required": [
    "cred_token"
  ],
  "definitions": {
    "credential_token": {
      "id": "credential_token",
      "type": "object",
      "title": "Credential: Token",
      "description": "A pair of a token, and an optional domain",
      "properties": {
        "domain": {
          "type": "string",
          "title": "Domain",
          "description": "The domain for the token"
        },
        "token": {
          "type": "string",
          "title": "Token",
          "displayType": "password",
          "description": "The shared token",
          "format": "password"
        }
      },
      "required": [
        "token"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)