from django.shortcuts import render
#incluir o mdelo que temos em models.py
from django.utils import timezone
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')   #posts é o nome do nosso queryset
    return render(request, 'blog/post_list.html', {'posts': posts}) # função render temos um paramentro request /tudo o que recebemos do usuário através da Internet
"""
criamos uma função (def) chamada post_list que leva a solicitação e irá retornar o valor
que recebe ao chamar outra função render que irá renderizar (montar) nosso modelo blog/post_list.html.
"""
