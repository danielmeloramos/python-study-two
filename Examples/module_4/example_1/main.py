#1- http
import requests

response = requests.get("https://aws.random.cat/meow")
data = response.json()
print(f"status: {response.status_code}")
print(f"data: {data}")