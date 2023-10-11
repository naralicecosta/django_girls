from django import forms

from .models import Post

class PostForm(forms.ModelForm): #PostForm nome do formulário / esse form é um ModelForm – forms.ModelForm é o responsável por essa parte.

    class Meta: # dizemos ao Django qual modelo deverá ser usado para criar este formulário (model = Post).
        model = Post 
        fields = ('title', 'text',) #campos que deverá ter no formulário