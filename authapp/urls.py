from django.urls import path
from .views import *

app_name = 'authapp'
urlpatterns = [
    path('',index),
    path('signup',signup,name='signup'),
    path('login',userLogin,name='login'),
    path('profile',profile,name='profile'),
    path('logout',usr_logout,name='logout'),

]