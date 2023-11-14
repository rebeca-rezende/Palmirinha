from ReceitaApp import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('receitas/', views.receitas, name='receitas'),
    path('receita/<int:id>', views.detalhes_receita, name='receita')
]


# path('caminho', nome da view(def), nome url)