from django.urls import path

from . import views

app_name = 'tweets'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:tweet_id>/', views.detail, name='detail'),
    path('post/', views.post, name='post'),
    path('create/', views.create, name='create'),
    path('<int:tweet_id>/destroy/', views.destroy, name="destroy"),
    path('<int:tweet_id>/edit/', views.edit, name='edit'),
    path('<int:tweet_id>/update/', views.update, name='update'),
    path('<int:user_id>/show/', views.show, name='show'),
]