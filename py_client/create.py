import requests

headers = {
    'Authorization': 'Bearer 7ec92e378b37d5f701b194b06a9efa5a53eafbf1'
}

endpoint = "http://127.0.0.1:8000/api/products/"
 
data = {
    "title": "this field is titlesss",
    "price": 32.99,
}
get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())