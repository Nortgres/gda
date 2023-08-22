from django.urls import path
from .views import post, postid


urlpatterns = [
    path('', post),
    path('post/<int:post_id>', postid)
]

