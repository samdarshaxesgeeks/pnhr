from nturl2path import url2pathname
from django.urls import path
from . import views

app_name = 'contract'


urlpatterns = [
    path('', views.contractlist, name='contract'),
    path('add_contract', views.CreateContract, name='add_contract')
]
