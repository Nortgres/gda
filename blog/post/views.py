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

def date_filter(request):
    start_date = request.GET.get('start_date')
    filter_type = request.GET.get('filter_type')
    f = None
    if start_date:
        if filter_type == 'gte':
            f = Post.objects.filter(created__gte=start_date)
        elif filter_type == 'lte':
            f = Post.objects.filter(created__lte=start_date)
    context = {
        'posts': f,
        'date': start_date
    }
    return render(request, 'date_filter.html', context)