from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from projects.owner import OwnerDeleteView
from projects.models.bot import BotComment
from projects.models.cosmic import CosmicComment
from projects.models.data_project import DataProjectComment
from projects.models.map import Population, CasesToday, Utility, Map, MapComment
from projects.forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin


class CommonView(View):
    model = None
    template_name = None
    project_name = None

    def _get_context(self):
        comments = self.model.objects.all().order_by('-updated_at')
        comment_form = CommentForm()
        context = {
            'comments': comments,
            'comment_count': len(comments),
            'comment_form': comment_form,
            'comment_create_link': f'projects:{self.project_name}_comment_create',
            'comment_delete_link': f'projects:{self.project_name}_comment_delete',
            'login_redirect_link': f'projects:{self.project_name}',
        }
        return context

    def get(self, response):
        return render(response, self.template_name, self._get_context())


class MapView(CommonView):
    model = MapComment
    template_name = 'map/map.html'
    project_name = 'map'

    def get(self, request):
        population = Population.objects.all()
        cases_today = CasesToday.objects.all()
        util = Utility.objects.all()
        _map = Map.objects.all()

        context = self._get_context()
        context.update({'population': population, 'cases': cases_today, 'util': util, 'map': _map})

        return render(request, self.template_name, context)


class BotView(CommonView):
    model = BotComment
    template_name = 'bot/bot.html'
    project_name = 'bot'


class CosmicPanelView(CommonView):
    model = CosmicComment
    template_name = 'cosmic/cosmic.html'
    project_name = 'cosmic'


class DataProjectView(CommonView):
    model = DataProjectComment
    template_name = 'data_project/data_project.html'
    project_name = 'data_project'


class CommentCreateView(LoginRequiredMixin, View):
    model = None
    redirect_url = None

    def post(self, request):
        comment = self.model(text=request.POST['comment'], owner=request.user)
        comment.save()
        return redirect(reverse(self.redirect_url))


class CommentDeleteView(OwnerDeleteView):
    template_name = 'comment/comment_delete.html'
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


class CosmicCommentMixin:
    model = CosmicComment
    redirect_url = 'projects:cosmic'


class DataProjectCommentMixin:
    model = DataProjectComment
    redirect_url = 'projects:data_project'


class MapCommentCreateView(MapCommentMixin, CommentCreateView):
    pass


class MapCommentDeleteView(MapCommentMixin, CommentDeleteView):
    pass


class BotCommentCreateView(BotCommentMixin, CommentCreateView):
    pass


class BotCommentDeleteView(BotCommentMixin, CommentDeleteView):
    pass


class CosmicCommentCreateView(CosmicCommentMixin, CommentCreateView):
    pass


class CosmicCommentDeleteView(CosmicCommentMixin, CommentDeleteView):
    pass


class DataProjectCommentCreateView(DataProjectCommentMixin, CommentCreateView):
    pass


class DataProjectCommentDeleteView(DataProjectCommentMixin, CommentDeleteView):
    pass

