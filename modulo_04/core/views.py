from django.shortcuts import render
# from django.http import HttpResponse <-- Não precisamos mais disso
# Create your views here.
def home(request):
    context = {
        'nome_usuario': 'Júnior',
        'tecnologias': ['Python', 'Django', 'HTML', 'CSS'],
    }
    # return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>")
    return render(request, 'home.html', context)
