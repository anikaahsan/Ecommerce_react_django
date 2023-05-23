from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from products import products
from .serializer import ProductSerializer
from .models import Product



@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/products/',
         '/api/products/create',

         '/api/products/upload',

          '/api/products/<id>/reviews/',

           '/api/products/top',
            '/api/products/<id>',

            '/api/products/delete/<id>',
             '/api/products/<update>/<id>',
    ]
    return Response(routes)

@api_view(['GET'])
def getProducts(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products,many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request,pk):
   
    # for product in products:   ##iteration allover list
    #     if product['_id']==pk: ##accessing  a key value pair in dictionary
           
    #         product=product
    #         return Response(product) ##for loop breaks
        product=Product.objects.get(pk=pk)
        serializer=ProductSerializer(product)
        return Response(serializer.data)
        
   
           

   







# def getRoutes(request):
#     routes=[
#         '/api/products/',
#          '/api/products/create',

#          '/api/products/upload',

#           '/api/products/<id>/reviews/',

#            '/api/products/top',
#             '/api/products/<id>',

#             '/api/products/delete/<id>',
#              '/api/products/<update>/<id>',
#     ]
    
#     return JsonResponse(products,safe=False)

# def getProducts(request):
#     return JsonResponse(products,safe=False)
