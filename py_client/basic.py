import requests

#endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint, json={"title":"None","content": "Hello World"})

print(get_response.text)

# HTTP Request -> HTML
# REST API HTTP Request ->
# JavaScript Object Nototion ~ Python Dict

#""print(get_response.json())
print(get_response.status_code)