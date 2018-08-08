from rest_framework import serializers
from .models import Clients, Message, Senders

class ClientsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clients
        fields = ('id','url', 'name', 'email')

class SendersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Senders
        fields = ('id', 'url', 'title')

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'url', 'title')