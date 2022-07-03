from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from strange.serializers import OrderSerializer, ItemSerializer, UserSerializer, EventSerializer, PunchSerializer
from strange.models import Order, Item, Payment, Event, Punch
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import api_view, action
from rest_framework.permissions import IsAuthenticated
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.
def index(request):
    return HttpResponse("This is the Backend Index")

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint for orders
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'buyer__id']

class ItemViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for items
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    @action(detail=False, methods=['POST'], name='Create orders')
    def create_orders(self, request):
        print(request.data)
        #this all matches and lines up with the info above
        order_items_data = request.data.pop('order_items')

        #changed user to buyer
        user_id = request.data.pop('buyer')
        buyer = User.objects.get(pk=user_id)

        order = Order.objects.create(buyer=buyer, **request.data)
        for oi in order_items_data:
            name = oi.pop('name')
            condition = oi.pop('condition')
            estimate = oi.pop('Estimate')
            actual = oi.pop('Actual')
            Item.objects.create(order=order, name=name, condition=condition, **oi)
            ##returning an httpresponse
        return HttpResponse(order)

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for Users
    """
    queryset=User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'groups__name']


class EventViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for Events
    """
    queryset=Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'name']


class PunchViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for Punches
    """
    queryset=Punch.objects.all()
    serializer_class = PunchSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'user__id']

    # def patch(self, replace, *args, **kwargs):
    #     instance = Punch.objects.get(pk=kwargs['id'])
    #     data = replace.data
    #     instance.time_out = data['time_out']

    #     instance.save()
    #     return HttpResponse(Punch.objects.get(pk=kwargs['id'])) 