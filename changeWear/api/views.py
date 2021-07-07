from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers,status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# modelos
from core.models import Producto
from .serializers import ProductoSerializer


# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])

def productos_ser(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])

def categoria_producto(request, pk):
    try:
        categoria = Producto.objects.filter(categoria = pk)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        
        serializers = ProductoSerializer(categoria, many=True)
        return Response(serializers.data) 