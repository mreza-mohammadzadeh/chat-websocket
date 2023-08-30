from django.urls import path
from chat.views import index

urlpatterns = [
    path("websocket", index, name='index'),
]
