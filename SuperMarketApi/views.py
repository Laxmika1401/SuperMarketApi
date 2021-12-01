from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item, Category, SubCategory
from .serializers import ItemSerializer
# Create your views here.


@api_view(['GET', 'POST', 'PATCH'])
def ItemView(request):
    if request.method == "GET":
        if 'category' in request.GET:
            categoryqs = Category.objects.get(title=request.GET['category'])
            category_qs = Item.objects.filter(category=categoryqs)
            serializer = ItemSerializer(category_qs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif 'subcategory' in request.GET:
            subcategoryqs = SubCategory.objects.get(
                title=request.GET['subcategory'])
            sub_itemqs = Item.objects.filter(subcategory=subcategoryqs)
            serializer = ItemSerializer(sub_itemqs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        Itemqs = Item.objects.all()
        serializer = ItemSerializer(Itemqs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PATCH":
        update_itemqs = Item.objects.get(name=request.data['name'])
        serializer = ItemSerializer(update_itemqs, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
