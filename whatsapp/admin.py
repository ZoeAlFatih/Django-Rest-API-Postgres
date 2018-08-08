from django.contrib import admin
from .models import Clients, Message, Senders

admin.site.register(Clients)
admin.site.register(Senders)
admin.site.register(Message)
