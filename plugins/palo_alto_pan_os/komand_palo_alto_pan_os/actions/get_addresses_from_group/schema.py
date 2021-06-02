# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get addresses from an address group"


class Input:
    DEVICE_NAME = "device_name"
    GROUP = "group"
    VIRTUAL_SYSTEM = "virtual_system"
    

class Output:
    ALL_ADDRESSES = "all_addresses"
    FQDN_ADDRESSES = "fqdn_addresses"
    IPV4_ADDRESSES = "ipv4_addresses"
    IPV6_ADDRESSES = "ipv6_addresses"
    SUCCESS = "success"
    

class GetAddressesFromGroupInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "device_name": {
      "type": "string",
      "title": "Device Name",
      "description": "Device name",
      "default": "localhost.localdomain",
      "order": 2
    },
    "group": {
      "type": "string",
      "title": "Group",
      "description": "Group name",
      "order": 1
    },
    "virtual_system": {
      "type": "string",
      "title": "Virtual System Name",
      "description": "Virtual system name",
      "default": "vsys1",
      "order": 3
    }
  },
  "required": [
    "device_name",
    "group",
    "virtual_system"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAddressesFromGroupOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "all_addresses": {
      "type": "array",
      "title": "All Addresses",
      "description": "Addresses currently in group",
      "items": {
        "type": "string"
      },
      "order": 5
    },
    "fqdn_addresses": {
      "type": "array",
      "title": "FQDN Addresses",
      "description": "FQDN addresses currently in group",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "ipv4_addresses": {
      "type": "array",
      "title": "IPv4 Addresses",
      "description": "IPv4 addresses currently in group",
      "items": {
        "type": "string"
      },
      "order": 3
    },
    "ipv6_addresses": {
      "type": "array",
      "title": "IPv6 Addresses",
      "description": "IPv6 addresses currently in group",
      "items": {
        "type": "string"
      },
      "order": 4
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Was operation successful",
      "order": 1
    }
  },
  "required": [
    "all_addresses",
    "fqdn_addresses",
    "ipv4_addresses",
    "ipv6_addresses",
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)