# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 13:25:10 2022

@author: usuario
"""

from django.urls import path
from.views import BlogListView, BlogDetailView, BlogCreateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
         path('post/new/', BlogCreateView.as_view(),name='post_new'),
         path('post/<int:pk>/', BlogDetailView.as_view(),name='post_detail'),    
         path('', BlogListView.as_view(),name='home1'),
              ]   
urlpatterns += staticfiles_urlpatterns()