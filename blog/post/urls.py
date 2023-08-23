from django.urls import path
from .views import post, postid, comment, commentid


urlpatterns = [
    path('', post),
    path('post/<int:post_id>', postid),
    path('comment', comment),
    path('comment/<int:comment_id>', commentid)
]

