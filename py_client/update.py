import requests

#endpoint = "https://httpbin.org/status/200/"
endpoint = "http://127.0.0.1:8000/api/products/8/update/"
headers = {
    'Authorization': 'Bearer 7ec92e378b37d5f701b194b06a9efa5a53eafbf1'
}
data = {
    "title":"new titlee",
    'price':129.99
}

get_response = requests.put(endpoint, data=data, headers=headers) #  json = data
