from django.shortcuts import render

from .serializers import TaskSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Task
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['GET','POST','DELETE'])
def getRoutes(request):
    routes=[
        'GET /api/get_task',
        'POST /api/add_task',
        'DELETE /api/delete_task/:id',
        'PUT /api/update_task/:id',

    ]
    return Response(routes) 

@api_view(['GET','POST','PUT','DELETE'])
def get_task(request):
    if request.method=='GET':
        context=Task.objects.all()
        serializer=TaskSerializers(context,many=True)
        return Response(serializer.data)

@api_view(['POST'])
def add_task(request):
    if request.method=='POST':        
        serializer=TaskSerializers(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def update_task(request,pk):
    if request.method=='PUT':
        context = get_object_or_404(Task, Name=pk)
        serializer=TaskSerializers(context,data=request.data,partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete_task(request,pk):
    if request.method=='DELETE':
        context=get_object_or_404(Task, Name=pk)
        context.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
