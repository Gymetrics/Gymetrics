from django.shortcuts import render
from .models import Stream 
from .serializers import StreamSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from channels import Group
import json

# Websocket update clients
def ws_update_stream(data):

    # data['live'] = str(data['live'])
    Group('streams').send({
        'text': json.dumps(data)
    })

# Create your views here.

def index(request):

    streams = Stream.objects.all()
    context = {'streams': streams}

    return render(request, 'dashboard/index.html', context)


@api_view(['GET', 'POST','PUT'])
def api_stream_view(request):

    if request.method == "GET": 
        streams = Stream.objects.all()
        serializer = StreamSerializer(streams, many=True)
        return Response(serializer.data)

    if request.method == "POST": 
        serializer = StreamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, content_type="application/json")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PUT":
        
        try:
            stream = Stream.objects.get(name=request.data['name'])
        except Stream.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)        

        serializer = StreamSerializer(stream, data=request.data)
        if serializer.is_valid():
            serializer.save()

            ws_update_stream(serializer.data)

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
