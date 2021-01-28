from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Lab, TimeService
from order.models import TestType
from order.serializer import TestTypeSerializer

class LabSerializer (ModelSerializer) :
    # types = TestTypeSerializer(many=True)
    # types = serializers.ListField(
    #     serializers.CharField(),
    #     allow_empty = True ,
    # )
    class Meta :
        model = Lab
        fields = ('name','end_point','api_key',)


    def create(self, validated_data):
        # print(validated_data)
        # types = validated_data.pop('types') 
        lab= Lab.objects.create(**validated_data)
        # for type in types :
        #     name = list(type.items())[0][1]
        #     print('\n\n',name,'\n\n')
        #     t = None
        #     try : 
        #         t = TestType.objects.create(name=name)
        #     except Exception :
        #         t = TestType.objects.get(name=name)

        #     t.lab.add(lab)

            
        return lab



class TimeServiceSerializer (ModelSerializer) :
    class Meta :
        model = TimeService
        fields = '__all__'

    def to_representation(self, instance):
        return {
            "id" : instance.id ,
            "date" : instance.date ,
            "stime" : instance.stime , 
            "etime" : instance.etime ,
            "expert" : str(instance.expert_snn.user.first_name) + " " + str (instance.expert_snn.user.last_name)
        }