import json

import requests

class Client:
    def get(self, url):
        response = requests.get(url)

        return response

    def post(self, url, data):
        response = requests.post(url, data=json.dumps(data))
        return response

    def delete(self, url):
        response = requests.delete(url)
        return response

    def put(self, url, data):
        response = requests.put(url, data=json.dumps(data))
        return response
