from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Auther
from .forms import AutherForm, BookFormSet

# Create your views here.

class CreateAutherView(CreateView):

    model = Auther
    form_class = AutherForm
    template_name = 'books/create-auther.html'
    success_url = reverse_lazy('books:create_auther')

    def get_context_data(self, **kwargs):
        context = super(CreateAutherView, self).get_context_data(**kwargs)
        context['inlines'] = BookFormSet()
        return context
