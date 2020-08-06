from django.urls import path,include
from django.contrib import admin
from post import views

app_name = "post"


urlpatterns = [
    path('', views.index, name='index'),
    path('ssl/', views.post, name='post'),
    path('<slug:slug>/', views.postdetail,name='postdetail'),
  
  

]