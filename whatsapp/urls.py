from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clients', views.ClientsView)
router.register('messages', views.MessageView)
router.register('senders', views.SendersView)

urlpatterns = [
    path('', include(router.urls))
]
