from django.urls import path
from .views import posts, postid, comments, commentsid


urlpatterns = [
    path('', posts, name='posts'),
    path('<int:post_id>', postid, name='postid'),
    path('', comments),
    path('<int:comment_id>', commentsid)
]

