from django.shortcuts import render
from .models import Gym 
from .serializers import GymSerializer
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

    gyms = Gym.objects.all()
    context = {'gyms': gyms}

    return render(request, 'dashboard/index.html', context)


@api_view(['GET', 'POST','PUT'])
def api_update_gym(request):

    if request.method == "GET": 
        gym = Gym.objects.get(location_name="Sky Gym")
        serializer = GymSerializer(gym)
        return Response(serializer.data)

    if request.method == "POST": 
        serializer = GymSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, content_type="application/json")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PUT":
        
        try:
            gym = Gym.objects.get(location_name=request.data['location_name'])
        except Gym.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)        

        serializer = GymSerializer(gym, data=request.data)
        if serializer.is_valid():
            serializer.save()

            ws_update_stream(serializer.data)

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
