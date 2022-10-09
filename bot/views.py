from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from bot.owner import OwnerDetailView, OwnerDeleteView
from bot.models import BotComment
from projects.forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin


class BotView(View):
    def get(self, response):
        comments = BotComment.objects.all().order_by('-updated_at')
        comment_form = CommentForm()
        context = {
        'comments': comments,
        'n': len(comments),
        'comment_form': comment_form
        }
        return render(response, 'bot/bot.html', context)


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request) :
        comment = BotComment(text=request.POST['comment'], owner=request.user)
        comment.save()
        return redirect(reverse('bot:bot'))


class CommentDeleteView(OwnerDeleteView):
    model = BotComment
    template_name = "map/comment_delete.html"

    def get_success_url(self):
        return reverse('bot:bot')
