from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), 
    path('post/<int:pk>/', views.post_detail, name='post_detail'), #criando uma url
    path('post/new/', views.post_new, name='post_new'),
        path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]
"""
views.post_list é o lugar correto aonde ir se alguém entra em seu site pelo endereço 'http://127.0.0.1:8000 /


post/ significa apenas que a URL deve começar com a palavra post seguida por /.

<int:pk> – diz que o Django espera um objeto do tipo inteiro e que vai transferi-lo para a view como uma variável chamada pk.
/ – por fim, precisamos adicionar uma / ao final da nossa URL.
"""