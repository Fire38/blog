from django.urls import path
from .views import index, article, register, login_view, logout_view, add_article, search_tag

urlpatterns = [
    path('', index, name='index'),
    path('article/<int:number>/', article, name='article'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('add_article/', add_article, name='add_article'),
    path('tag/<tag_name>', search_tag, name='search_tag')
]
