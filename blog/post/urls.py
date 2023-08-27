from django.urls import path
from .views import posts, postid, comments, commentsid


urlpatterns = [
    path('', posts),
    path('<int:post_id>', postid),
    path('', comments),
    path('<int:comment_id>', commentsid)
]

