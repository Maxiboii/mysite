from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from projects.owner import OwnerDeleteView
from projects.models.bot import BotComment
from projects.models.map import Population, CasesToday, Utility, Map, MapComment
from projects.forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin


class MapView(View):
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
            'comment_create_link': 'projects:map_comment_create',
            'comment_delete_link': 'projects:map_comment_delete',
            'login_redirect_link': 'projects:map',
        }
        return render(request, self.template_name, context)


class BotView(View):
    def get(self, response):
        comments = BotComment.objects.all().order_by('-updated_at')
        comment_form = CommentForm()
        context = {
            'comments': comments,
            'comment_count': len(comments),
            'comment_form': comment_form,
            'comment_create_link': 'projects:bot_comment_create',
            'comment_delete_link': 'projects:bot_comment_delete',
            'login_redirect_link': 'projects:bot',
        }
        return render(response, 'bot/bot.html', context)


class CommentCreateView(LoginRequiredMixin, View):
    model = None
    redirect_url = None

    def post(self, request):
        comment = self.model(text=request.POST['comment'], owner=request.user)
        comment.save()
        return redirect(reverse(self.redirect_url))


class CommentDeleteView(OwnerDeleteView):
    template_name = 'home/comment_delete.html'
    model = None
    redirect_url = None

    def get_success_url(self):
        return reverse(self.redirect_url)

    def render_to_response(self, context, **response_kwargs):
        context['redirect_url'] = self.redirect_url
        return super().render_to_response(context, **response_kwargs)


class MapCommentMixin:
    model = MapComment
    redirect_url = 'projects:map'


class BotCommentMixin:
    model = BotComment
    redirect_url = 'projects:bot'


class MapCommentCreateView(MapCommentMixin, CommentCreateView):
    pass


class MapCommentDeleteView(MapCommentMixin, CommentDeleteView):
    pass


class BotCommentCreateView(BotCommentMixin, CommentCreateView):
    pass


class BotCommentDeleteView(BotCommentMixin, CommentDeleteView):
    pass
