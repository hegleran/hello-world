import json
import requests

# ASA
url = "https://192.168.10.100/api/objects/networkobjects"

payload = "{\r\n  \"host\": {\r\n    \"kind\": \"IPv4Address\",\r\n    \"value\": \"100.1.1.1\"\r\n  },\r\n  \"kind\": \"object#NetworkObj\",\r\n  \"name\": \"Development\",\r\n  \"objectId\": \"Development\"\r\n}"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic ZW5hYmxlXzE6Y2lzY28="
    }

response = requests.request("POST", url, data=payload, verify=False, headers=headers)

print(response.text)

# NXOS
"""
Modify these please
"""
url='http://192.168.10.60/ins'
switchuser='admin'
switchpassword='Passw0rd1'

myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "conf t ;vlan 600 ;name Construction ;vlan 700 ;name Analysis ",
    "output_format": "json"
  }
}
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()


# IOSXE
url = "http://192.168.10.80/restconf/api/config/native/ip/route"

payload = "{ \"ned:route\": {\n\t\"ip-route-interface-forwarding-list\": [\n\t\t{ \"prefix\": \"216.48.1.0\",\n\t\t \"mask\": \"255.255.255.0\",\n\t\t \"fwd-list\": [ { \"fwd\": \"10.1.1.1\" } ]\n\t\t }\n\t\t]\n\t}\n}"
headers = {
    'Content-Type': "application/vnd.yang.data+json",
    'Accept': "application/vnd.yang.data+json",
    'Authorization': "Basic YWRtaW46Y2lzY28="
    }

response = requests.request("PUT", url, data=payload, headers=headers)

print(response.text)
