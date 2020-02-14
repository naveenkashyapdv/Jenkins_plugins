import requests
import json
base_url = "https://plugins.jenkins.io/api/plugin"
for i in open("/var/jenkins-plugins/Untitled-1"):
    url = base_url + "/" + i.strip()
    response = requests.request("GET", url)
    print("'" + i.strip() + "'=> '" + json.loads(response.text)["version"] + "',")