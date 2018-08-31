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

url = "http://192.168.10.1/api/node/mo/uni/tn-testtenant.json"

payload = "{\"fvTenant\":{\"attributes\":{\"dn\":\"uni/tn-testtenant\",\"name\":\"testtenant\",\"rn\":\"tn-testtenant\",\"status\":\"created\"},\"children\":[]}}"
cookie = {"APIC-cookie": tokenfromlogin}

response = requests.request("POST", url, data=payload, cookies=cookie)

print(response.text)
