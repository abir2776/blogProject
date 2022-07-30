from django.urls import path
from . import views

app_name='app_blog'

urlpatterns = [
     path('',views.BlogList.as_view(),name='blog_list'),
     path('write/',views.CreateBlog.as_view(),name='create_blog'),
     path('details/<slug:slug>',views.blog_details,name='blog_details'),
     path('liked/<pk>/',views.liked,name='liked_post'),
     path('unliked/<pk>',views.unliked,name='unliked_post'),
     path('my_blogs/',views.MyBlogs.as_view(),name='my_blogs'),
     path('edit_blog/<pk>/',views.UpdateBlog.as_view(),name='edit_blog'),
]