from venv import logger

from django.shortcuts import render
import pprint
pp = pprint.PrettyPrinter(indent=4)
from rest_framework import generics
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from stores_data.models import User

from .serializers import UserSerializer,ParentSerializer,ChildSerializer

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/userlist/',
		'Individual User View':'/users/<int:pk>/',
		'Create Parent User':'user-create/parent/',
		'Create Child User':'user-create/new/child/',
		'Update':'/user-update/<str:pk>/',
		'Delete':'/user-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def userList(request):
	users = User.objects.all().order_by('-id')
	serializer = UserSerializer(users,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def userIndividualView(request, pk):
	users = User.objects.get(id=pk)
	serializer = UserSerializer(users, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def parentUserCreate(request):
	serializer = ParentSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def childUserCreate(request):
	serializer = ChildSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def userUpdate(request, pk):
	users = User.objects.get(id=pk)
	serializer = UserSerializer(instance=users, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def userDelete(request, pk):
	users = User.objects.get(id=pk)
	users.delete()

	return Response('User is succsesfully deleted!')

'''class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserSpecificAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    pp.pprint(str(queryset))
    for query in queryset:
        pp.pprint("Data"+str(query.belong_to))
        if query.belong_to != '':
            serializer_class = ParentSerializer
        elif query.belong_to == '':
            serializer_class = ChildSerializer

class NewParentCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('-id')[:1]  # latest user
    serializer_class = ParentSerializer

class NewChildCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('-id')[:1]  # latest user
    serializer_class = ChildSerializer '''

