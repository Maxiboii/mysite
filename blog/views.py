from django.shortcuts import render
from django.views import View

from .models import Post


class PostsView(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'blog/posts.html', context)


class PostView(View):
    def get(self, request, _id):
        post = Post.objects.get(id=_id)
        context = {
            'post': post,
        }
        return render(request, 'blog/post.html', context)
