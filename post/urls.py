from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),

    path('create_post/', views.create_post, name='create_post'),
    path('delete_post/', views.delete_post, name='delete_post'),
    path('detail_post/', views.detail_post, name='detail_post'),
    path('update_post/', views.update_post, name='update_post'),
]
