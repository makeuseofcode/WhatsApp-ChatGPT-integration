from django.urls import path
from .views import *

urlpatterns = [
    path('chat', OpenAIGPTView.as_view()),
]