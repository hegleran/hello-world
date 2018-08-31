import requests

url = "http://192.168.10.1/api/aaaLogin.json"

payload = "{\n\t\"aaaUser\": {\n\t\t\"attributes\": {\n\t\t\t\"name\" : \"admin\",\n\t\t\t\"pwd\" : \"ciscoapic\"\n\t\t}\n\t}\n}"
cookie = {"APIC-cookie": "M5Ejog37L+e7A7Mk4456b/e8OHzlkNjje+Pyv+RUpl2dzeJNFgAALyYiy7Ijy6hTwKmwzdhYV1hzlFC56xqM1tZhc761G5QsBdmIX3AYG2DSv9NWvkf9YZzwoCoXuLwd/rZas12nUO808N8moRApKU/h3uDYLjRM1ekWkwP5y2M="}

response = requests.request("POST", url, data=payload, cookies=cookie)

print(response.text)