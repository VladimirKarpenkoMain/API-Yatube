from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentListCreateView, CommentRetrieveUpdateDestroyView, GroupViewSet, FollowViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='post_comments'),
    path('posts/<int:post_id>/comments/<int:comment_id>/', CommentRetrieveUpdateDestroyView.as_view(), name='post_comment_detail'),
    path('groups/', GroupViewSet.as_view({'get': 'list'})),
    path('groups/<int:group_id>/', GroupViewSet.as_view({'get': 'retrieve'})),
    path('follow/', FollowViewSet.as_view({'get': 'list', 'post': 'create'}))
]
