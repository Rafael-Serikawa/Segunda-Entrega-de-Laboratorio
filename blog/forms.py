from django import forms
from .models import Post, Comment, Category

class PostForm(forms.ModelForm):

    categorias = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False # Permite criar um post sem categoria, se desejar
    )

    class Meta:
        model = Post
        fields = ['titulo', 'conteudo', 'categorias']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['texto']