from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, BloodExpert, Lab, TimeService
from django.db import transaction 
# Create your views here.


class UserSignup (APIView) :

    def post (self, *args, **kwargs) :
        data = self.request.data
        try :
            User.objects.create(data['snn'],data['password'],data['firstName'],\
                                data['lastName'],data['sex'],data['email'],data['phone'])
            return Response(data={
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
            lab = Lab.objectst.get(name=data['lab'])
            BloodExpert.objects.create(data['snn'],data['password'],data['firstName'],\
                                data['lastName'],data['sex'],data['email'],data['phone'],lab=lab)
            return Response(data={
                "message" : "Expert successfuly inserted!"
            }, status=status.HTTP_201_CREATED)

        except Exception as exc :
            return Response(data={
                "message" : str(exc)
                }, status=status.HTTP_201_CREATED)


class LabSignup (APIView) :

    def post (self, *args, **kwargs) :
        data = self.request.data
        try :
            Lab.objects.create(data['name'],data['end_point'],data['api_ley'])
            return Response(data={
                "message" : "Lab successfuly inserted!"
            }, status=status.HTTP_201_CREATED)

        except Exception as exc :
            return Response(data={
                "message" : str(exc)
                }, status=status.HTTP_201_CREATED)


class TimeServiceRegistery (APIView) :

    def post (self, *args, **kwargs) :
        data = self.request.data
        try :
            expert = BloodExpert.objects.get(snn=data['expert_snn'])
            TimeService.objects.create(expert_snn = expert, date = data['date'], stime = data['stime'],\
                                etime = data['etime'], evailable = data['evailable'])
            return Response(data={
                "message" : "Serive time successfuly added!"
            }, status=status.HTTP_201_CREATED)

        except Exception as exc :
            return Response(data={
                "message" : str(exc)
                }, status=status.HTTP_201_CREATED)

    @transaction.atomic
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




        

        
        