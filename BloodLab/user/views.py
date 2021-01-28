from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, BloodExpert, Lab, TimeService
from .serializer import LabSerializer
from django.db import transaction 
from order.models import Order, TestType
from order.serializer import TestTypeSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User as AuthUser
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

# class RefreshUserToken(APIView) :
#     get get


class UserSignup (APIView) :

    def post (self, *args, **kwargs) :
        data = self.request.data
        try :
            new_user = AuthUser.objects.create_user(username=data['snn'], password=data['password'], email=data['email'],\
                 first_name=data['firstName'], last_name = data['lastName'])
            User.objects.create(user=new_user, phone = data['phone'], sex = data['sex'])
            refresh = RefreshToken.for_user(new_user)
            return Response(data={
                "access" : str(refresh.access_token) ,
                "refresh" : str(refresh) ,
                "message" : "User successfuly inserted!"
            }, status=status.HTTP_201_CREATED)

        except Exception as exc :
            return Response(data={
                "message" : str(exc)
                }, status=status.HTTP_201_CREATED)

        
        
class BloodExpertSignup (APIView) :

    def post (self, *args, **kwargs) :
        data = self.request.data
        try :
            lab = Lab.objects.get(name=data['lab'])
            new_user = AuthUser.objects.create_user(username=data['snn'], password=data['password'], email=data['email'],\
                 first_name=data['firstName'], last_name = data['lastName'])
            BloodExpert.objects.create(user=new_user, phone = data['phone'], sex = data['sex'], lab=lab)

            refresh = RefreshToken.for_user(new_user)
            return Response(data={
                "access" : str(refresh.access_token) ,
                "refresh" : str(refresh) ,
                "message" : "Expert successfuly inserted!"
            }, status=status.HTTP_201_CREATED)

        except Exception as exc :
            return Response(data={
                "message" : str(exc)
                }, status=status.HTTP_201_CREATED)


class LabSignup (APIView) :

    def post (self, *args, **kwargs) :
        data = self.request.data
        types = data.pop('types') 
        

        lab_serializer = LabSerializer(data=data)
        if lab_serializer.is_valid() :
            lab = lab_serializer.save()
            for testtype in types :
                t , _= TestType.objects.get_or_create(name=testtype['name'])
                t.lab.add(lab)
            return Response(data={
                "message" : f"{lab} successfuly inserted!"
            }, status=status.HTTP_201_CREATED)
        else :
            return Response(data= lab_serializer.errors
                , status=status.HTTP_400_BAD_REQUEST)


class TimeServiceRegistery (APIView) :

    permission_classes = (IsAuthenticated,)
    def post (self, *args, **kwargs) :
        data = self.request.data
        try :
            expert = BloodExpert.objects.get(user__username=self.request.user.username)
            TimeService.objects.create(expert_snn = expert, date = data['date'], stime = data['stime'],\
                                etime = data['etime'], evailable = data['evailable'])
            return Response(data={
                "message" : "Serive time successfuly added!"
            }, status=status.HTTP_201_CREATED)

        except Exception as exc :
            return Response(data={
                "message" : str(exc)
                }, status=status.HTTP_201_CREATED)

    def put (self, *arg, **kwargs) :
        data = self.request.data 
        try : 
            time_service = TimeService.objects.get(expert_snn = data['expert_snn'], date = data['date'],\
                                                   stime = data['stime'], etime = data['etime'])
                                                   
            time_service.date = data['new_date'] 
            time_service.stime = data['new_stime'] 
            time_service.etime = data['new_etime'] 
            time_service.available = data['evailable'] 

            time_service.save()

            return Response(
                data={
                    "expert_snn" : time_service.expert_snn ,
                    "date" : time_service.date ,
                    "stime" : time_service.stime ,
                    "edtime" : time_service.etime ,
                    "available" : time_service.available
                } ,
                status=status.HTTP_200_OK
            )
        except Exception as exc : 
            return Response(data={
                "message" : str(exc)
                }, status=status.HTTP_201_CREATED)
   

        