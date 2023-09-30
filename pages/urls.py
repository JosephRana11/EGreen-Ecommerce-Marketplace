from django.urls import path
from .views import home_view , login_view , logout_view , about_view , contact_view

urlpatterns = [
  path('' , home_view , name = 'home'),
  path('login' , login_view , name='login'),
  path('logut' , logout_view , name='logout'),
  path('about' , about_view , name='about'),
  path('contact' , contact_view , name='contact'),
]