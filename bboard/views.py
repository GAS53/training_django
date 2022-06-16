from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Bb
from django.shortcuts import get_object_or_404

class BoardView(TemplateView):
    paginate_by = 2
    template_name = 'bboard/index.html'
    # model = Bb


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bbs"] = Bb.objects.all()
        return context

    # def get_queryset(self):
    #     return super().get_queryset()