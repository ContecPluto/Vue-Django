from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_article, name='create_article'),
    path('detail/<int:article_pk>/', views.detail, name='detail'),
    path('detail/<int:article_pk>/comment/', views.comment_create, name='comment'),
    path('detail/<int:article_pk>/comment/<int:comment_pk>/', views.comment_delete, name='comment_delete'),
]
