from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from bboard.forms import BbForm
from .models import Bb, Rubric
from django.shortcuts import get_object_or_404

class BoardView(TemplateView):
    paginate_by = 5
    template_name = 'bboard/index.html'
    # model = Bb


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bbs"] = Bb.objects.all()
        context["rubrics"] = Rubric.objects.all()
        return context


class By_rubric(TemplateView):
    template_name = 'bboard/by_rubric.html'


    def get_context_data(self, rubric_id,  **kwargs):
        context = super().get_context_data(**kwargs)
        context["rubrics"] = Rubric.objects.all()
        context["bbs"] = Bb.objects.filter(rubric=rubric_id)
        context["current_rubric"] = Rubric.objects.get(pk=rubric_id)
        return context

    
class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('board:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context