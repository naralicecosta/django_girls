# imports são importações de outros arquivos.
# facilita pois não precisamos copiar e colar todo o arquivo, apenas pedaçoes que queremos
from django.conf import settings
from django.db import models
from django.utils import timezone

#modelo de postagem para o blog, é um objeto

class Post (models.Model): #class é a palavra que mostra que estamos definindo um objeto/ post é o nome do nosso modelo
    # / models.Model significa que o Post é um modelo de Django, então o Django sabe que ele deve ser salvo no banco de dados.

    """definindo nossas propriedades e o tipo de cada uma"""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # este é um link para outro modelo.
    title = models.CharField(max_length=200) #CharField texto com número limitado de caracteres. no nosso, o maximo é 200 para nome de titulo
    text = models.TextField() #texto sem limite fixo, ideal para conteúdo do blog
    created_date = models.DateTimeField(default=timezone.now) # este é uma data e hora.
    published_Date = models.DateTimeField(blank=True, null=True)


    def publish(self): #metodo publish/ def declara uma função e publish seu nome
        self.published_Date = timezone.now()
        self.save()

        def __str__(self):
            return self.title
        