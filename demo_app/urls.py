"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from demo_app import views

urlpatterns = [
    path('', views.index),
    path('example-path/', views.index),
    path('example-block/', views.block),

    path('add-blog-post/', views.add_blog_post),
    path('remove-blog-post/<int:post_id>/', views.remove_blog_post),
    path('list-blog-posts/', views.list_blog_posts),

    path('add/', views.add_form),
]
