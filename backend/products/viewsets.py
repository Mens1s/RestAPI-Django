from rest_framework import mixins, viewsets

from .models import Product
from .serializers import ProductSerializer

'''
    get -> list -> queryset
    get -> retrieve -> Product Instance Detail View
    post -> create -> New Instance
    put -> Update
    patch -> Partial Update
    Delete -> Destroy
'''
class ProductViewSet(viewsets.ModelViewSet):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

'''
    get -> list -> queryset
    get -> retrieve -> Product Instance Detail View
'''    
class ProductGenericViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
product_list_view = ProductViewSet.as_view({'get':'list'})
product_detail_view = ProductViewSet.as_view({'get':'retrieve'})

