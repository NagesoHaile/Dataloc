from django.shortcuts import render

from rest_framework.decorators import action
from rest_framework.response import Response 
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin,UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import CreateAPIView,UpdateAPIView,RetrieveAPIView,GenericAPIView
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from .serializers import UserSerializer


class UserView(CreateAPIView,RetrieveAPIView,UpdateAPIView,GenericAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


    # @action(detail=False, methods=['GET','PUT'])
    # def me(self,request):
    #     user = UserProfile.objects.get_or_create(id==request.user.id)
    #     serializer = UserSerializer(user)
    #     if request.method == 'GET':
    #         return Response(serializer.data)
    #     elif request.method == 'PUT':
    #         serializer = UserSerializer(user,data= request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data)



    
    

