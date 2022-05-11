
from django.urls import path
from .views import HomeView, ADetailView, AddPostView, UpdatePostView, DeletePostView, SearchResultsView
from .views import LikeView, AddCommentView, UpdateCommentView, DeleteCommentView, AboutView, LatestNewsView

urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('article/<int:pk>/', ADetailView.as_view(), name="article_detail"),
    path('add_post/', AddPostView.as_view(), name = 'add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name = 'update'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name = 'delete'),
    path('like/<int:pk>', LikeView, name='like_post'), 
    path('article/<slug:pk>/add_comment/',AddCommentView.as_view(), name='add_comment'),
    path('article/<slug:pk>/update_comment/',UpdateCommentView.as_view(), name='updateC'),
    path('article/<slug:pk>/delete_comment/',DeleteCommentView.as_view(), name='deleteC'),
    path('about/', AboutView, name='about'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('latest/', LatestNewsView.as_view(), name='latest'),
]