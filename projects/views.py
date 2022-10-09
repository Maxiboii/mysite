from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from bot.owner import OwnerDetailView, OwnerDeleteView
from projects.models.map import Population, CasesToday, Utility, Map, MapComment
from projects.forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin


class MapView(OwnerDetailView):
    model = Map
    template_name = "map/map.html"

    def get(self, request, *args, **kwargs):
        comments = MapComment.objects.all().order_by('-updated_at')
        comment_form = CommentForm()
        population = Population.objects.all()
        casestoday = CasesToday.objects.all()
        util = Utility.objects.all()
        map = Map.objects.all()
        context = {
            'comments': comments,
            'comment_count': len(comments),
            'comment_form': comment_form,
            'population': population,
            'cases': casestoday,
            'util': util,
            'map': map,
            'comment_create_link': 'map:map_comment_create',
            'comment_delete_link': 'map:map_comment_delete',
            'login_redirect_link': 'map:map',
        }
        return render(request, self.template_name, context)


class MapCommentCreateView(LoginRequiredMixin, View):
    def post(self, request) :
        comment = MapComment(text=request.POST['comment'], owner=request.user)
        comment.save()
        return redirect(reverse('map:map'))


class MapCommentDeleteView(OwnerDeleteView):
    model = MapComment
    template_name = "map/comment_delete.html"

    def get_success_url(self):
        return reverse('map:map')
