from django.urls import path
from .views import *
urlpatterns = [
    path('',predictor,name='predictor'),
    path('result/',formInfo,name='result')
    
]
