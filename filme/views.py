from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Filme
from .forms import FilmeForm

class FilmeListView(ListView):
    model = Filme
    template_name = 'filme/listar.html'
    context_object_name = 'filmes'

class FilmeDetailView(DetailView):
    model = Filme
    template_name = 'filme/detalhe.html'
    context_object_name = 'filme'

class FilmeCreateView(CreateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'filme/form.html'
    success_url = reverse_lazy('filme_listar')

class FilmeUpdateView(UpdateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'filme/form.html'
    success_url = reverse_lazy('filme_listar')

class FilmeDeleteView(DeleteView):
    model = Filme
    template_name = 'filme/confirm_delete.html'
    success_url = reverse_lazy('filme_listar')
