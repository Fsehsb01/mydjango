from django.urls import path
from . import views
app_name='myweb'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('look/', views.look,name='look'),
    path('', views.detail, name='detail'),
    path('hello/',views.lokk,name='lokk'),
]
