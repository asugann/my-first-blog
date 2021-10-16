from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.core.paginator import Paginator


# Create your views here.


def index(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, "index.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def dragons(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, "dragons.html", {"posts": posts})


def dragonshistory(request):
    return render(request, "dragonshistory.html", {})
