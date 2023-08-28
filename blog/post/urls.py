from django.urls import path
from .views import posts, postid, comments, date_filter

app_name = 'posts'
urlpatterns = [
    path('', posts, name='posts'),
    path('<int:post_id>', postid, name='postid'),
    path('', comments),
    path('date-filter/', date_filter, name='date_filter')
]