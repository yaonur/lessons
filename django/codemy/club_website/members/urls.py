from django.urls import path
from . import views

app_name = 'members'
urlpatterns = [
    path('', views.login_view, name='login')
]
