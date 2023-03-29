from django.shortcuts import render

# Create your views here.


# HTTP REQUEST
def home(request):
    # 'Respondendo' a "request" do usuário
    return render(request, 'recipes/pages/home.html', {
        "name": "Nikolas de Almeida"
    })
