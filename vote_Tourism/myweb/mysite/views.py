from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-vote')[:3]

    return render(request, 'index.html', locals())

def listing(request):
    posts = Post.objects.all().order_by('-vote')

    return render(request, 'listing.html', locals())

def disp_detail(request, id):
    p = Post.objects.all().get(id=id)

    return render(request, 'detail.html', locals())