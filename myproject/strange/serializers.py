from django.contrib.auth.models import User, Group
from strange.models import Order, Item, Payment, Event, Punch
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'total_paid', 
            'pub_date', 
            'suggested', 
            'delta', 
            'seller', 
            'note', 
            'buyer', 
            'method',
            'item_set'
            ]
        depth = 1


class ItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    class Meta:
        model = Item
        fields = [
            'id',
            'name',
            'set_name',
            'order'
        ]
        depth = 1

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 
            'last_login', 
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'is_active', 
            'groups'
        ]
        depth = 1

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'name',
            'date',
            'time',
            'format',
            'prizeSupport',
            'entry',
            'registrationLink',
            'location',
            'qualifications',
            'top8',
            'cap'
        ]

class PunchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Punch
        fields = [
            'id',
            'user',
            'time_in',
            'time_out',
            'type'
        ]