from django.urls import path
from . import views
urlpatterns = [
    path('api/despesas/', views.DespesaListCreate.as_view()),
]