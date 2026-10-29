from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/novo/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/editar/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/apagar/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/comentar/', views.add_comment_to_post, name='add_comment_to_post'),
]
