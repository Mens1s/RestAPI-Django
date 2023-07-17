import requests
headers = {
    'Authorization': 'Bearer 7ec92e378b37d5f701b194b06a9efa5a53eafbf1'
}
product_id = input("Enter id : ")

try:
    product_id = int(product_id)
except:
    print(f"{product_id} not a valid id")
    product_id = None
    
if product_id:
            
    endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete"

    get_response = requests.delete(endpoint, headers=headers)

    print(get_response.status_code, get_response.status_code == 204)
