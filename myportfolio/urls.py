from django.urls import path
from . import views
from .more.hire_me import hire_me

urlpatterns = [
    path('', views.index, name='index'),
    path('hire_me/', hire_me, name='hire_me'),
    path('blog', views.blog, name='blog')
]
