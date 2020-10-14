from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from ads.owner import OwnerDetailView, OwnerDeleteView
from django.conf import settings
from map.models import Population, CasesToday, Utility, Map, MapComment
from map.forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.humanize.templatetags.humanize import naturaltime


class MapView(OwnerDetailView):
    model = Map
    template_name = "map/map.html"
    def get(self, request) :
        comments = MapComment.objects.all().order_by('-updated_at')
        comment_form = CommentForm()
        population = Population.objects.all()
        casestoday = CasesToday.objects.all()
        util = Utility.objects.all()
        map = Map.objects.all()
        context = {
        'comments': comments,
        'n': len(comments),
        'comment_form': comment_form,
        'population': population,
        'cases': casestoday,
        'util': util,
        'map': map
        }
        return render(request, self.template_name, context)


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request) :
        comment = MapComment(text=request.POST['comment'], owner=request.user)
        comment.save()
        return redirect(reverse('map:map'))


class CommentDeleteView(OwnerDeleteView):
    model = MapComment
    template_name = "map/comment_delete.html"

    def get_success_url(self):
        return reverse('map:map')
