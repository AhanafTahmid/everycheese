from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Cheese

from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
class CheeseListView(ListView):
    model = Cheese

class CheeseDetailView(DetailView):
    model = Cheese

class CheeseCreateView(CreateView,LoginRequiredMixin):
    model = Cheese
    fields = ['name', 'description','country_of_origin']
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)