from django.shortcuts import render
from .models import Produto

# Create your views here.

def lista_produtos(request):
    produtos = Produto.objects.all()  # busca todos os produtos
    return render(request, 'loja_informatica/lista_produtos.html', {'produtos': produtos})
