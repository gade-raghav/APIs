from django.shortcuts import render
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import HumanSerializer
from .models import Human

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'All Data':'/all/',
        'Detail':'one/<str:id>',
        'Create':'/create',
        'Update':'/update/<str:id>',
        'Delete':'/delete/<str:id>',
    }
    
    return Response(api_urls)

@api_view(['GET'])    
def all(request):
    tasks = Human.objects.all()
    serializer = HumanSerializer(tasks, many=True )
    return Response(serializer.data)

@api_view(['GET'])    
def one(request, id):
    human = Human.objects.get(id=id)
    serializer = HumanSerializer(human, many=False )
    return Response(serializer.data)


@api_view(['POST'])    
def create(request):
    serializer = HumanSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def update(request,id):
    human = Human.objects.get(id=id)
    serializer = HumanSerializer(instance=human,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete(request,id):
    human = Human.objects.get(id=id)
    human.delete()

    return Response("Successfully deleted.")
