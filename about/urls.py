from django.urls import path
from .views import *


urlpatterns = [
    path('one/', BookApiDetailList.as_view(), name='one'),
    path('two/<int:pk>/', BookApiDeleteList.as_view(), name='two'),
]