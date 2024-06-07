from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view() , name='login'),
]