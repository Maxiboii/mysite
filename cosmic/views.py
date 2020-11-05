from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from cosmic.owner import OwnerDetailView, OwnerDeleteView
from django.conf import settings
from cosmic.models import PanelComment
from map.forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.humanize.templatetags.humanize import naturaltime


# Create your views here.
class PanelView(View):
    def get(self, response):
        comments = PanelComment.objects.all().order_by('-updated_at')
        comment_form = CommentForm()
        context = {
        'comments': comments,
        'n': len(comments),
        'comment_form': comment_form
        }
        return render(response, 'cosmic/index.html', context)

class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request) :
        comment = PanelComment(text=request.POST['comment'], owner=request.user)
        comment.save()
        return redirect(reverse('cosmic:panel'))


class CommentDeleteView(OwnerDeleteView):
    model = PanelComment
    template_name = "map/comment_delete.html"

    def get_success_url(self):
        return reverse('cosmic:panel')
