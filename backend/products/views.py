from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

from api.mixins import StaffEditorPermissionMixin
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content= serializer.validated_data.get('content') or None
         
        if content is None:
            content = title
        if not Product.objects.all().filter(title = title).exists():
            serializer.save(content=content)
        
product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(StaffEditorPermissionMixin, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # lookup_field = 'pk'
    
product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'    

    def perform_update(self, serializer):
        instance = serializer.save()
        
        if not instance.content:
            instance.content = instance.title
            

product_update_view = ProductUpdateAPIView.as_view()

class ProductDeleteAPIView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        
product_delete_view = ProductDeleteAPIView.as_view()        


# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
# product_list_view = ProductListAPIView.as_view() 


class ProductMixinView(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    allowed_methods = ['GET','POST','PUT','DELETE']
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        if pk :
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
product_mixin_view = ProductMixinView.as_view()

@api_view(['GET', 'POST'])
def product_alt_view(request, pk = None, *args, **kwargs):
    method = request.method
    
    if method == "GET":
        if pk is not None:
            # detail view
           
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)

        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    
    if method == "POST":
        '''
        DEF API VIEW
        '''
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # instance = serializer.save(commit=False) # delete commit=False when it's ready
            # instance = form.save() : same thing
            title = serializer.validated_data.get('title')
            content= serializer.validated_data.get('content') or None
            
            if content is None:
                content = title
            if not Product.objects.all().filter(title = title).exists():
                serializer.save(content=content)
                return Response(serializer.data)
            return Response({"invalid":"your data has already used"}, status = 400)
        
        return Response({"invalid":"not valid data"}, status=400)