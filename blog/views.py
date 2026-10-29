from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

# Read (Listar todos)
def post_list(request):
    posts = Post.objects.all().order_by('-data_postagem')
    return render(request, 'blog/post_list.html', {'posts': posts})

# Read (Detalhes individuais)
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# Create
def post_create(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        Post.objects.create(titulo=titulo, conteudo=conteudo)
        return redirect('post_list')
    return render(request, 'blog/post_form.html')

# Update
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.titulo = request.POST.get('titulo')
        post.conteudo = request.POST.get('conteudo')
        post.save()
        return redirect('post_detail', pk=post.pk)
    return render(request, 'blog/post_form.html', {'post': post})

# Delete
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})
