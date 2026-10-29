from django.urls import reverse_lazy
from django.views import generic
from .models import Post, Category
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['titulo', 'conteudo', 'categorias']
    template_name = 'blog/post_form.html'

# R - Read (Listagem)
class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-data_postagem']

# R - Read (Detalhes)
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# View para Criar Post (Protegida)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = '/'

# View para Editar Post (Protegida)
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = '/'

# View para Excluir Post (Protegida)
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.autor = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form, 'post': post})

# View para listar todas as categorias
class CategoriaListView(generic.ListView):
    model = Category
    template_name = 'blog/categoria_list.html'
    context_object_name = 'categorias'

# View para a página individual da categoria
def categoria_detail(request, pk):
    categoria = get_object_or_404(Category, pk=pk) # Retorna 404 se não existir
    posts = categoria.posts.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'categoria': categoria})