import requests
import time

url = 'https://www.virustotal.com/vtapi/v2/url/report'

url1 = open(r"<file_name>")
for x in url1:
 try:
  url1 = x.rstrip()
  print(url1)
  params = {'apikey': '<api_key>', 'resource':url1}
  response = requests.get(url, params=params)
  print(response.json()["positives"])
  time.sleep(16)
 except:
  pass