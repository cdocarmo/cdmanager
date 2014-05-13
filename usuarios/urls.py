from django.conf.urls import *

urlpatterns = patterns('usuarios.views',
   url(
       r'^forgot-password/$', 
       'forgot_password', 
       name="forgot-password",
       
   ),
   url( r'^change-password/$', 'change_password',name="change-password") ,
   
)