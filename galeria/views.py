from django.shortcuts import render, get_object_or_404

from galeria.models import Fotografia

# Rota para chamar minha pagina principal e exibir os dados do banco


def index(request):
    fotografias = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {'cards': fotografias})


def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})
