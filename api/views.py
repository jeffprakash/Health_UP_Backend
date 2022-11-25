from imaplib import _Authenticator
from xmlrpc.client import ResponseError
from django.shortcuts import render
from .serializers import UserSerializer,dataSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets ,permissions
from django.contrib import auth
from .models import User,Profile


# Create your views here.
@api_view(['GET'])
def get_details(request):                                          #api to get details of patient
    users=Profile.objects.all()
    serializer =dataSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_user_list(request):
    users=User.objects.all()                                        #api to get all users
    serializer =UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def signup(request):
    serializer= UserSerializer(data=request.data)
    if serializer.is_valid():
         user_id = serializer.validated_data.get('user_id')
         #user_exists=User.objects.get(username=username)
         
         serializer.save()
         
         return Response({"signup":"success"})
    else:
        return Response(serializer.errors)


@api_view(['GET'])
def get_user_by_num(request,pk):                              #api to get patient list by id
    num=Profile.objects.get(id=pk)
    serializer =dataSerializer(num, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def form(request):
    serializer= dataSerializer(data=request.data)
    if serializer.is_valid():
         user_id = serializer.validated_data.get('user_id')
         #user_exists=User.objects.get(username=username)
         
         serializer.save()
         
         return Response({"data":"added"})
    else:
        return Response(serializer.errors)