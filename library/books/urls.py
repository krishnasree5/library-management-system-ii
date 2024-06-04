from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    path('', views.search, name='search'),
    path('<int:pk>/', views.detail, name='detail')
]