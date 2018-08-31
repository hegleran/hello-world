import requests
import json

url = "http://192.168.10.1/api/aaaLogin.json"

payload = "{\n\t\"aaaUser\": {\n\t\t\"attributes\": {\n\t\t\t\"name\" : \"admin\",\n\t\t\t\"pwd\" : \"ciscoapic\"\n\t\t}\n\t}\n}"
headers = {
    'Content-Type': "application/vnd.yang.data+json",
    'Accept': "application/vnd.yang.data+json",
    'Authorization': "Basic YWRtaW46Y2lzY29hcGlj"
    }

response = requests.request("POST", url, data=payload, headers=headers)

json_response = json.loads(response.text)
#print(json_response)['imdata'][0]['aaaLogin']['attributes']['token']
tokenfromlogin = (json_response['imdata'][0]['aaaLogin']['attributes']['token'])


# tenant
url = "http://192.168.10.1/api/node/mo/uni/tn-acme.json"

payload = "{\"fvTenant\":{\"attributes\":{\"dn\":\"uni/tn-acme\",\"name\":\"acme\",\"rn\":\"tn-acme\",\"status\":\"created\"},\"children\":[]}}"
cookie = {"APIC-cookie": tokenfromlogin}

response = requests.request("POST", url, data=payload, cookies=cookie)

print(response.text)

# AP
url = "http://192.168.10.1/api/node/mo/uni/tn-acme/ap-Accounting.json"

payload = "{\r\n\t\"fvAp\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-acme/ap-Accounting\",\r\n\t\t\t\"name\": \"Accounting\",\r\n\t\t\t\"rn\": \"ap-Accounting\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": []\r\n\t}\r\n}"
cookie = {"APIC-cookie": tokenfromlogin}

response = requests.request("POST", url, data=payload, cookies=cookie)

print(response.text)

# EPG
url = "http://192.168.10.1/api/node/mo/uni/tn-acme/ap-Accounting/epg-Payroll.json"

payload = "{\r\n\t\"fvAEPg\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-acme/ap-Accounting/epg-Payroll\",\r\n\t\t\t\"name\": \"Payroll\",\r\n\t\t\t\"rn\": \"epg-Payroll\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": [{\r\n\t\t\t\"fvCrtrn\": {\r\n\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\"dn\": \"uni/tn-acme/ap-Accounting/epg-Payroll/crtrn\",\r\n\t\t\t\t\t\"name\": \"default\",\r\n\t\t\t\t\t\"rn\": \"crtrn\",\r\n\t\t\t\t\t\"status\": \"created,modified\"\r\n\t\t\t\t},\r\n\t\t\t\t\"children\": []\r\n\t\t\t}\r\n\t\t}]\r\n\t}\r\n}"

response = requests.request("POST", url, data=payload, cookies=cookie)

print(response.text)

url = "http://192.168.10.1/api/node/mo/uni/tn-acme/ap-Accounting/epg-Bills.json"

payload = "{\r\n\t\"fvAEPg\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-acme/ap-Accounting/epg-Bills\",\r\n\t\t\t\"name\": \"Bills\",\r\n\t\t\t\"rn\": \"epg-Bills\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": [{\r\n\t\t\t\"fvCrtrn\": {\r\n\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\"dn\": \"uni/tn-acme/ap-Accounting/epg-Bills/crtrn\",\r\n\t\t\t\t\t\"name\": \"default\",\r\n\t\t\t\t\t\"rn\": \"crtrn\",\r\n\t\t\t\t\t\"status\": \"created,modified\"\r\n\t\t\t\t},\r\n\t\t\t\t\"children\": []\r\n\t\t\t}\r\n\t\t}]\r\n\t}\r\n}"

response = requests.request("POST", url, data=payload, cookies=cookie)

print(response.text)
