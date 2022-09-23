from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name='index'),
    path("ins/",ins,name='ins'),
    path("dash/",Dashboard,name='dash'),
    path("accounts/login/",UserLogin,name='login'),
    path("logout/",Logout,name='logout'),
    path("register/",Register,name='register'),

    path('provider/',provider,name='provider')

]