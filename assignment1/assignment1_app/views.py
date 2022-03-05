from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404,JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from .models import CoffeeRoaster
from .serializers import CoffeeRoasterSerializer,CoffeeRoasterViewSerializer
from drf_yasg.utils import swagger_auto_schema
@swagger_auto_schema()
@api_view(['GET','POST'])
def coffeelist(request):
    if request.method == "GET":
        coffeeroasterlist = CoffeeRoaster.objects.all()
        serializer = CoffeeRoasterViewSerializer(coffeeroasterlist,many = True)
        return Response({"total":coffeeroasterlist.count(), "coffees" : serializer.data},status = status.HTTP_200_OK)
    elif(request.method == "POST"):
        serializer = CoffeeRoasterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":0,"message":"New coffee added","id":serializer.data["id"]},status = status.HTTP_201_CREATED)
#            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
@swagger_auto_schema()
@api_view(['GET','PUT','DELETE','PATCH'])
def coffee_detail(request,pk):
    try:
        coffee =  CoffeeRoaster.objects.get(pk=pk)
    except:
        raise Http404
    if request.method == "GET":
        serializer = CoffeeRoasterSerializer(coffee)
        return Response(serializer.data,status = status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = CoffeeRoasterSerializer(coffee,data=request.data,partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":0,"message":"Coffee updated"},status = status.HTTP_200_OK)
            #(serializer.data,status)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        coffee.delete()
        return Response({"status":0,"message":"Coffee deleted"},status = status.HTTP_200_OK)
    elif request.method == "PATCH":
        serializer = CoffeeRoasterSerializer(coffee,data= request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":0,"message":"Coffee modified"},status = status.HTTP_200_OK)
            #return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
