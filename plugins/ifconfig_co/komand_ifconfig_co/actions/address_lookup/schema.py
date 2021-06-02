# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Lookup Public IP Address"


class Input:
    pass

class Output:
    ADDRESS = "address"
    ADDRESS_DECIMAL = "address_decimal"
    CITY = "city"
    COUNTRY = "country"
    HOSTNAME = "hostname"
    

class AddressLookupInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddressLookupOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "Public IP Address",
      "description": "Public IP address",
      "order": 1
    },
    "address_decimal": {
      "type": "integer",
      "title": "Decimal Address",
      "description": "Public IP address in decimal",
      "order": 5
    },
    "city": {
      "type": "string",
      "title": "City",
      "description": "City",
      "order": 2
    },
    "country": {
      "type": "string",
      "title": "Country",
      "description": "Country",
      "order": 3
    },
    "hostname": {
      "type": "string",
      "title": "Hostname",
      "description": "Hostname",
      "order": 4
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)