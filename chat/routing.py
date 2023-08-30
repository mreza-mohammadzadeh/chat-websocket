from django.urls import path, re_path
from chat import consumers

websocket_urlpatterns = [
    path('ws/', consumers.ChatConsumer.as_asgi())
]
