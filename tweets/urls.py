from django.urls import path

from . import views

app_name = 'tweets'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('post/', views.post, name='post'),
    path('create/', views.create, name='create'),
    path('<int:tweet_id>/destroy/', views.destroy, name="destroy"),
    path('<int:pk>/edit/', views.EditView.as_view(), name='edit'),
    path('<int:tweet_id>/update/', views.update, name='update'),
]