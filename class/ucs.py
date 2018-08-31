import requests

url = "http://192.168.10.90/nuova"

payload = "<configResolveDn cookie=\"null\" inHierarchical=\"false\" dn=\"sys/chassis-6\"/>"
headers = {
    'Content-Type': "application/vnd.yang.data+json",
    'Accept': "application/vnd.yang.data+json",
    'Authorization': "Basic Y2lzY286Y2lzY28="
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
