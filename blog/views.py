from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from blog.owner import OwnerDeleteView

from .models import Post, BlogComment
from map.forms import CommentForm


class PostsView(View):
    def get(self, request):
        posts = Post.objects.all()
        comments = BlogComment.objects.all().order_by('-updated_at')
        comment_form = CommentForm()
        context = {
            'posts': posts,
            'comments': comments,
            'n': len(comments),
            'comment_form': comment_form
        }
        return render(request, 'blog/posts.html', context)


class PostView(View):
    def get(self, request, _id):
        post = Post.objects.get(id=_id)
        context = {
            'post': post,
        }
        return render(request, 'blog/post.html', context)


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request):
        comment = BlogComment(text=request.POST['comment'], owner=request.user)
        comment.save()
        return redirect(reverse('blog:blog'))


class CommentDeleteView(OwnerDeleteView):
    model = BlogComment
    template_name = "map/comment_delete.html"

    def get_success_url(self):
        return reverse('blog:blog')
