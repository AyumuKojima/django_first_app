from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('log_in/', views.log_in, name='log_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('register/', views.register, name='register'),
]