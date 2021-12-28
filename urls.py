from django.contrib import admin
from django.urls import path, include
from Home import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="Home"),
    path('login', views.loginUser, name="loginUser"),
    path('logout', views.logoutUser, name="logoutUser")
    
]
