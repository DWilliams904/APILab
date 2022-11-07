import requests
import json

url = "https://icanhazdadjoke.com"

intro = "Here's a random joke: "
payload={}
headers = { 
	'Accept': 'application/json'
	}

response = requests.request("GET", url, headers=headers, data=payload)

responseJson = response.json()['joke']

print(intro + responseJson)


