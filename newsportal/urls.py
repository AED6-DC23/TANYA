from django.urls import path

from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('create/', PostCreate.as_view(), name='Create'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('<int:pk>/comments', comment, name='Comments'),
    path('comm/', MyCommentList.as_view(), name='comm'),
    path('<int:pk>/edit', PostEdit.as_view(), name='edit'),
    path('<int:pk>/delete', PostDel.as_view(), name='delete'),
    path('<int:pk>/addcomment', CommCreate.as_view(), name='addcomm'),
    path('profile', profile, name='profile'),
    path('comments/<int:pk>', OneComm.as_view(), name='onecomm'),
    path('comments/<int:pk>/delete', CommDel.as_view(), name='delcomm'),
    path('comments/<int:pk>/confirm', CommConfirm.as_view(), name='confirm'),
]
