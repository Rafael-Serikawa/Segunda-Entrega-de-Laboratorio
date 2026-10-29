from django.urls import reverse_lazy
from django.views import generic
from .models import Post
from .forms import PostForm

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

# C - Create
class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

# U - Update
class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

# D - Delete (Usa a página de confirmação automaticamente)
class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
    