from django.urls import path
from posts import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='posts-list-page'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='posts-details-page'),
    path('posts/create/', views.PostCreateView.as_view(), name='create'),
    path('<int:pk>/create_comment/', views.create_comment, name='create_comment'),
]
