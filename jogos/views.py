from django.shortcuts import render, get_object_or_404
from .models import Equipe, Modalidade


def index(request):
    equipes = Equipe.objects.all()
    modalidades = Modalidade.objects.all()
    return render(request, 'jogos/index.html', {'equipes': equipes, 'modalidades': modalidades})


def equipe(request, id):
    equipe = get_object_or_404(Equipe, id=id)
    atletas = equipe.atletas.all()
    return render(request, 'jogos/equipe.html', {'equipe': equipe, 'atletas': atletas})


def modalidade(request, id):
    modalidade = get_object_or_404(Modalidade, id=id)
    atletas = modalidade.atletas.all()
    return render(request, 'jogos/modalidade.html', {'modalidade': modalidade, 'atletas': atletas})
