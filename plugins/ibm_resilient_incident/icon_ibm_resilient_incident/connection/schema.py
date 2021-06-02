# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    CREDS = "creds"
    HOSTNAME = "hostname"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "creds": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Credentials",
      "description": "Username and password",
      "order": 2
    },
    "hostname": {
      "type": "string",
      "title": "Hostname",
      "description": "Hostname for the Resilient application",
      "order": 1
    }
  },
  "required": [
    "creds"
  ],
  "definitions": {
    "credential_username_password": {
      "id": "credential_username_password",
      "type": "object",
      "title": "Credential: Username and Password",
      "description": "A username and password combination",
      "properties": {
        "password": {
          "type": "string",
          "title": "Password",
          "displayType": "password",
          "description": "The password",
          "format": "password"
        },
        "username": {
          "type": "string",
          "title": "Username",
          "description": "The username to log in with"
        }
      },
      "required": [
        "username",
        "password"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)