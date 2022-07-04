from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    # login
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('send/email/verification', views.send_email_verification_code, name='send_email_verification_code'),
    path('email/verify', views.verify_email, name='verify_email'),
    path('home',views.home,name='home'),
    path('password/change',views.password_change,name='password_change')

]
