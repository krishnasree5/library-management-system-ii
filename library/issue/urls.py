from django.urls import path
from . import views

app_name = 'issue'

urlpatterns = [
    path('new/', views.new_issue, name='new')
]