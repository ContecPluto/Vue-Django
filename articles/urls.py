from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_article, name='create_article'),
    path('detail/<int:article_pk>/', views.detail, name='detail'),
    path('update/<int:article_pk>/', views.update_article, name='update_article'),
    path('comment/<int:article_pk>/', views.comment_create, name='comment'),
    path('comment/<int:comment_pk>/', views.comment_delete, name='comment_delete'),
    path('hashtags/', views.hashtag_list, name="hashtag_list")
]
