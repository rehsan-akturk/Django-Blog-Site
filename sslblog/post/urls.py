from django.urls import path,include
from django.contrib import admin
from post import views

app_name = "post"


urlpatterns = [
    path('', views.index, name='index'),
    path('ssl/', views.post, name='post'),
    #path('category/comodo-ssl', views.show_category, name='category'),
    #path('category/sslrapid/', views.show_category, name='category'),
    path('category/<path:hierarchy>/', views.show_category,name='category'),
    path('<slug:slug>/', views.postdetail,name='postdetail'),
    
  

]