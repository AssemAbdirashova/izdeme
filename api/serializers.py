from rest_framework import serializers
from api.models import Service, Statistics_week
from django.contrib.auth import authenticate
from rest_framework import exceptions
from django.contrib.auth.models import User

from api.models import Course


class CourseSerializer(serializers.ModelSerializer):
    # category = CategorySerializer2(read_only=True)
    # category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics_week
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    # category = CategorySerializer2(read_only=True)
    #category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Service
        fields = '__all__'


#
# class OrderSerializer(serializers.ModelSerializer):
#     id=serializers.IntegerField(read_only=True)
#     class Meta:
#         model = Order
#         fields = ('id', 'username', 'items')
#
#
#
#
#
# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     username = serializers.CharField()
#     password = serializers.CharField()
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     # address = serializers.CharField()
#     # phone = serializers.CharField()
#
#     def create(self, validated_data):
#         user = User.objects.create(username=validated_data.get('username'),
#                                    password=validated_data.get('password'),
#                                    first_name=validated_data.get('first_name'),
#                                    last_name=validated_data.get('last_name'),
#                                    # address=validated_data.get('address'),
#                                    # phone=validated_data.get('phone'),
#                                    )
#
#         return user

    # def update(self, instance, validated_data):
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.password = validated_data.get('password', instance.password)
    #     instance.firstName = validated_data.get('firstName', instance.firstname)
    #     instance.lastName = validated_data.get('lastName', instance.lastName)
    #     instance.address = validated_data.get('address', instance.address)
    #     instance.phone = validated_data.get('phone', instance.phone)
    #     instance.save()
    #     return instance

    # def validate(self, data):
    #     username = data.get("username", "")
    #     password = data.get("password", "")
    #
    #     if username and password:
    #         user = authenticate(username=username, password=password)
    #         if user:
    #             if user.is_active:
    #                 data["user"] = user
    #             else:
    #                 msg = "User is deactivated."
    #                 raise exceptions.ValidationError(msg)
    #         else:
    #             msg = "Unable to login with given credentials."
    #             raise exceptions.ValidationError(msg)
    #     else:
    #         msg = "Must provide username and password both."
    #         raise exceptions.ValidationError(msg)
    #     return data


#
# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()
#
#     def validate(self, data):
#         username = data.get("username", "")
#         password = data.get("password", "")
#
#         if username and password:
#             user = authenticate(username=username, password=password)
#             if user:
#                 if user.is_active:
#                     data["user"] = user
#                 else:
#                     msg = "User is deactivated."
#                     raise exceptions.ValidationError(msg)
#             else:
#                 msg = "Unable to login with given credentials."
#                 raise exceptions.ValidationError(msg)
#         else:
#             msg = "Must provide username and password both."
#             raise exceptions.ValidationError(msg)
#         return data
