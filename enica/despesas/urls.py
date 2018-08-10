from django.urls import path
from . import views
urlpatterns = [
    path('api/despesas/', views.DespesaListCreate.as_view()),
    path('api/categorias/', views.CategoriaListCreate.as_view()),
    path('api/parcelas/', views.ParcelaListCreate.as_view())
]