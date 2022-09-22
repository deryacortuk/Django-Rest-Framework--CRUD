from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
path('',views.apiOverview, name="api"),
 path('article/', views.ArticleListView.as_view(), name='article_list'),
  path('add/',views.ArticleCreate.as_view()),    
 path('article/<id>/', views.ArticleDetailView.as_view(), name='article_detail'),
 
]
