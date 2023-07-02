# import json
# from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.serializers import ProductSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    '''
    DEF API VIEW
    '''
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save(commit=False) # delete commit=False when it's ready
        # instance = form.save() : same thing
        print(serializer.data)
        return Response(serializer.data)
    
    return Response({"invalid":"not valid data"}, status=400)
    
'''
    # DRF API VIEW
    # first_data = Product.objects.filter(id=request.GET['id']).get()
    # data = request.data
    
    # model_data = Product.objects.all().order_by("?").first()
    # data = {}
    
    # if first_data:
    #     model_data = first_data
        
    # if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
        #data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price']) # ('id', 'title')
        # serialization
        # model instance (model_data)
        # turn a Python dict
        # return JSON to my clien
        # instance = model_data
        # data = ProductSerializer(instance).data
        

    print(request.GET) # params in the url ?abc=123
    print(request.POST)
    
    body = request.body # byte string of JSON data 
    # body -> is json data which sent by client
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    
    data["params"] = dict(request.GET)
    data["headers"] = dict(request.headers)
    data["content_type"] = request.content_type
    
    return JsonResponse(data)
    '''
    
    