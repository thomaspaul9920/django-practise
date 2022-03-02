from unicodedata import name
from django.urls import path
from . import views
app_name = 'atm'
urlpatterns = [
    path('', views.index, name='login'),
    path('signup/',views.signup, name='signup'),
    path('<int:user_id>/main/', views.main, name='main'),
    path('<int:user_id>/deposit/', views.deposit, name='deposit'),
    path('<int:user_id>/withdraw/', views.withdraw, name='withdraw'),
]