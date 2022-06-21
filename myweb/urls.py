from django.urls import path
from . import views
app_name='myweb'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.look,name='look'),
    path('detail/', views.detail, name='detail'),
]
