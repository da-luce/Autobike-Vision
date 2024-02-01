import requests
import json

print("hello")

url = "http://localhost:8000"

# Data to be written
dictionary = {
	"name": "sathiyajith",
	"rollno": 56,
	"cgpa": 8.6,
	"phonenumber": "9976770500"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4).encode('utf-8')

# Writing to sample.json
#with open("sample.json", "w") as outfile:
#	outfile.write(json_object)
     
json_load = json.loads(json_object)

print("BEFORE POST")

x = ''
y = ''
try:
    x = requests.post(url, json=json_load)
except requests.exceptions.ConnectionError:
    print("Connection refused")

print("AFTER POST")