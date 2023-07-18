from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('book/', views.book, name='book'),
    # path('menu/', views.menu, name='menu'),
    # path('users/<str:name>/<int:id>/', views.users, name='users'),
    # path('user', views.user, name='user'),
]
