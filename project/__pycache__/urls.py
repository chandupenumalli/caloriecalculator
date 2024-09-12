from django.contrib import admin
from django.urls import path
from app1.views import index, about, login, register, doregister, logincheck, userhome, adminhome, contact, viewusers, modify,contactmessage

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name='index'),
    path('register/', register, name='register'),
    path('register/doregister/', doregister, name='doregister'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('logincheck/', logincheck, name='logincheck'),
    path('userhome/', userhome, name='userhome'),
    path('adminhome/', adminhome, name='adminhome'),
    path('contact/', contact, name='contact'),
    path('viewusers/', viewusers, name='viewusers'),
    path('modify/', modify, name='modify'),
    path('contactmessage/',contactmessage)
]
