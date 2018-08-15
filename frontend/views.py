from django.shortcuts import render

# Create your views here.
def euGostoDeCamelCase():
    return "VIADO!"

def index(request):
    return render(request, 'frontend/index.html')