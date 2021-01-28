from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import transaction 
from .models import Order, TestType, Test
from .serializer import TestTypeSerializer ,OrderCreateSerializer, OrderRetriveSerializer, LabSerializer
from user.models import Lab, User, TimeService, BloodExpert
from user.serializer import TimeServiceSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User as AuthUser
from rest_framework_simplejwt.tokens import RefreshToken


from django.db.models import Count
# Create your views here.


class GetOrCreateTestType(APIView) :

    def post (self, *args, **kwargs) :
        serializer = TestTypeSerializer(data= self.request.data)

        if serializer.is_valid() :
            serializer.save()
            return Response(
                data= {'message':'Test Type inserted successfully!'},
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            data={'message':'Some error has been occurred!'},
            status=status.HTTP_400_BAD_REQUEST
        )


    def get (self, *args, **kwargs) :
        serializer = TestTypeSerializer(TestType.objects.all(), many=True) 

        return Response(
            data = serializer.data ,
            status=  status.HTTP_200_OK
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
        if serializer.is_valid(raise_exception=True) :
            order = serializer.save()

            return Response(
                data = {
                    "message": "saved" ,
                    "id" : order.id
                } ,
                status=status.HTTP_200_OK
            )

     
class GetLabsDoingSpecificTestsAndReservasion(APIView) :
    permission_class = (IsAuthenticated,)

    def get (self, *args, **kwargs) :
        requested_types = self.request.data
        labs = Lab.objects.all()

        for type in requested_types['types'] :
            labs = labs.filter(testtypes__name = type)
        data = LabSerializer(labs, many=True).data
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )

    def post (self, *args, **kwargs) :
        time_id = self.request.data.get('time_id')
        ts = TimeService.objects.get(id=time_id)
        ts.evailable = False 
        ts.save()

        order_id = self.request.data.get('order_id')
        order = Order.objects.get(id=order_id)
        order.expert = ts.expert_snn
        order.save()

        return Response(
            data=  {"message":f"Time service {time_id} reserved."} ,
            status= status.HTTP_200_OK
        )
        

class GetLabFreeTimeServices (APIView) :
    permission_class = (IsAuthenticated,)

    def get (self, *args, **kwargs) :
        # serializer = LabSerializer(data= self.request.data) 
        try:
            t = TimeService.objects.filter(expert_snn__lab__name=self.request.data.get('lab'), evailable=True)

            serializer = TimeServiceSerializer(t, many=True)

            return Response(data=serializer.data,
                status=status.HTTP_200_OK)
            
        except Exception as exc :
            
            return Response(data={"message":str(exc)},
                status=status.HTTP_400_BAD_REQUEST)
