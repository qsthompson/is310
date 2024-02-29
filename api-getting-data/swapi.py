#get data
#print item 
#store as csv
import requests
import json
import random

r = requests.get('https://swapi.dev/api/planets/' + str(random.randint(0,60))).text
data = json.loads(r)
print(data)
out = json.dumps(data, indent=4)
with open("planet.json", "w") as f:
	f.write(out)
