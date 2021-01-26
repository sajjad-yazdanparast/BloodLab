from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import transaction 
from .models import Order
from .serializer import TestTypeSerializer ,OrderCreateSerializer, OrderRetriveSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User as AuthUser
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.


class TestType(APIView) :

    def post (self, *args, **kwargs) :
        serializer = TestTypeSerializer(data= self.request.data)

        if serializer.is_valid() :
            return Response(
                data= {'message':'Test Type inserted successfully!'},
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            data={'message':'Some error has been occurred!'},
            status=status.HTTP_400_BAD_REQUEST
        )




class GetOrCreateOrders (APIView) :


    permission_classes = (IsAuthenticated, )
    def get(self, *args, **kwargs) :
        serializer = OrderRetriveSerializer(Order.objects.filter(tests__user__user=self.request.user), many=True)
        return Response(
            data= serializer.data ,
            status=status.HTTP_200_OK
        )

    def post (self, *args, **kwargs) :
        data = self.request.data 
        data['user'] = self.request.user.username
        serializer = OrderCreateSerializer(data= data) 
        # print(serializer.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()

            return Response(
                data = {"message": "saved"} ,
                status=status.HTTP_200_OK
            )

     