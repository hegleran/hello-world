import requests

url = "http://192.168.10.1/api/node/mo/uni/tn-testtenant.json"

payload = "{\r\n\t\"fvTenant\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-testtenant\",\r\n\t\t\t\"name\": \"testtenant\",\r\n\t\t\t\"rn\": \"tn-testtenant\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": []\r\n\t}\r\n}"
cookie = {"/flfh7u69fQ+IVfDZwuCedpoTsj61MklZ/jWHYIHCrgFlmNlTnu9n2bXBZehNJTOu2TCnGebpwu7rVBtHQkiOJytDYGHqNoknfTNSYq2G+sd7v9Wu7E22uS6vbOoq2zRLBMOPc8ZEkV4MAV8Zxhnk1No07DlbKr8iwDurqjtfL0="}
headers = {
    'Content-Type': "application/vnd.yang.data+json",
    'Accept': "application/vnd.yang.data+json",
    'Authorization': "Basic YWRtaW46Y2lzY28="
    }

response = requests.request("POST", url, data=payload, cookies=cookie)

print(response.text)
