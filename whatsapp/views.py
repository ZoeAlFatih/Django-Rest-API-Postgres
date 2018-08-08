from django.shortcuts import render
from rest_framework import viewsets
from .models import Clients, Message, Senders
from .serializer import ClientsSerializer, MessageSerializer, SendersSerializer

class ClientsView(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer

class SendersView(viewsets.ModelViewSet):
    queryset = Senders.objects.all()
    serializer_class = SendersSerializer

class MessageView(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

