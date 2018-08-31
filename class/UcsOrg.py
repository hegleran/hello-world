import requests

url = "http://192.168.10.90/nuova"

payload = "<configConfMos\ncookie=\"1535719807/180d079f-da5e-40c9-a7ea-648ea585e4aa\"\ninHierarchical=\"false\">\n    <inConfigs>\n<pair key=\"org-root/org-PythonMaster\">\n    <orgOrg\n    name=\"PythonMaster\"\n    dn=\"org-root/org-PythonMaster\"\n    \n    status=\"created\"\n    \n    sacl=\"addchild,del,mod\">\n    </orgOrg>\n</pair>\n    </inConfigs>\n</configConfMos>"
headers = {
    'Content-Type': "application/vnd.yang.data+json",
    'Accept': "application/vnd.yang.data+json",
    'Authorization': "Basic Y2lzY286Y2lzY28="
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
