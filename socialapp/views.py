

from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-hora')  # exibe do mais novo pro mais antigo
    return render(request, 'social/index.html', {'posts': posts})

def nova_postagem(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        titulo = request.POST['titulo']
        conteudo = request.POST['conteudo']

        Post.objects.create(usuario=usuario, titulo=titulo, conteudo=conteudo)

        return redirect('index')

    return render(request, 'social/nova_postagem.html')

def contato(request):
    return render(request, 'social/contact.html')

def sobre(request):
    return render(request, 'social/about.html')

def postar(request):
    return render(request, 'social/post.html')

def base(request):
    return render(request, 'social/base.html')

