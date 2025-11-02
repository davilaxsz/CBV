from django.urls import path
from .views import (
    FilmeListView,
    FilmeDetailView,
    FilmeCreateView,
    FilmeUpdateView,
    FilmeDeleteView
)

urlpatterns = [
    path('', FilmeListView.as_view(), name='filme_listar'),
    path('<int:pk>/', FilmeDetailView.as_view(), name='filme_detalhe'),
    path('novo/', FilmeCreateView.as_view(), name='filme_criar'),
    path('<int:pk>/editar/', FilmeUpdateView.as_view(), name='filme_editar'),
    path('<int:pk>/excluir/', FilmeDeleteView.as_view(), name='filme_excluir'),
]
