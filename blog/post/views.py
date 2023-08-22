from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


# Create your views here.
def post(request):
    f = Post.objects.all()
    # return HttpResponse(f)
    context = {
        'post': f
    }
    return render(request, 'index.html', context)


def postid(request, post_id):
    f = get_object_or_404(Post, pk=post_id)
    return HttpResponse(f)
