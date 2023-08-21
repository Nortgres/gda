from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def post(request):
    f = Post.objects.all()
    return HttpResponse(f)
