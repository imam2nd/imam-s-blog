from django.urls import path,re_path
from . import views


urlpatterns = [
    path('', views.article_list, name="article_list"),
    path('khit/', views.khit),
    path('create', views.article_create, name= "create"),
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail, name='detail'),
]
