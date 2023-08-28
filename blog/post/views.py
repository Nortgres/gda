from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Comments


# Create your views here.
def posts(request):
    f = Post.objects.all()
    # return HttpResponse(f)
    context = {
        'posts': f
    }
    return render(request, 'index.html', context)


def postid(request, post_id):
    f = get_object_or_404(Post, pk=post_id)
    context = {
        'postid': f
    }
    #return HttpResponse(f)
    return render(request, 'post.html', context)

def comments(request):
    f = Comments.objects.all()
    return HttpResponse(f)

def commentsid(request, comment_id):
    f = get_object_or_404(Comments, pk=commens_id)
    return HttpResponse(f)