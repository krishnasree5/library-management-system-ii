from django.urls import path
from . import views

app_name = 'issue'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('notifications/', views.notifications, name='notifications'),
]