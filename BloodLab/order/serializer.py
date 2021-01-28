from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import * 
from user.models import User

class TestTypeSerializer(ModelSerializer) :
    class Meta :
        model = TestType
        fields = ('name',)

class LabSerializer (ModelSerializer) :
    class Meta :
        model = Lab
        fields = ('name',)


class TestSerializer (ModelSerializer) :
    # type = TestTypeSerializer()

    # lab = LabSerializer()
    # type = serializers.CharField()
    # lab = serializers.CharField()
    class Meta :
        model = Test
        fields = ('type','lab','result')



class OrderCreateSerializer(ModelSerializer):
    tests = TestSerializer(many=True)
    user = serializers.CharField()
    class Meta:
        model = Order
        fields = ('status', 'price', 'longitude', 'latitude', 'tests', 'user')


    # def create(self, validated_data):
    #     print(*validated_data)
    def create(self, validated_data):
        user = User.objects.get(user__username=validated_data.pop('user'))
        tests = validated_data.pop('tests') 
        order = Order.objects.create(**validated_data)

        for test in tests :
            Test.objects.create(user=user, order=order, **test)
        
        return order
        print('\n\n',validated_data,'\n\n')
        # return super().create(validated_data)

        
class OrderRetriveSerializer (ModelSerializer) :
    # test = TestSerializer(source='test_set', many=True)
    # test = serializers.PrimaryKeyRelatedField(many=True)
    class Meta : 
        model = Order 
        fields = '__all__'

    
    def to_representation(self, instance):
        serializer = TestSerializer()
        return {
            "test" : TestSerializer(instance.tests, many=True).data ,
            "price" : instance.price ,
            "status" : self.Meta.model.CHOISES[instance.status][1] ,
            "longitude" : instance.longitude , 
            "latitude" : instance.latitude
        } 
