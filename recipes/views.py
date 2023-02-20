from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# HTTP REQUEST
def home(request):
    # 'Respondendo' a "request" do usuário
    return render(request, 'recipes/home.html')


# HTTP REQUEST
def sobre(request):
    return HttpResponse('Sobre dentro da app')


# HTTP REQUEST
def contato(request):
    return HttpResponse('Contato dentro da app')
