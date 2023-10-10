numSoma = 2+5 
print(numSoma)

# Deixando maiusculo / upper()
nome = 'nara'
nome_maiusculo = nome.upper()
print(nome_maiusculo)

# tamanho de uma string / len ()
print(len("ola teste"))
#len diz o número de letrasm frases, e etc

# listas / []
lottery = [3,43,12,30,59]
print(len(lottery))

# organizando em ordem / sort ()
lottery = [3,43,12,30,59]
lottery.sort()
print(lottery)

# invertendo a ordem / reverse ()
lottery = [3,43,12,30,59]
lottery.reverse()
print(lottery)

# para adicionar  algo a lista / append ()
lottery = [3,43,12,30,59]
lottery.append(200)
print(lottery)

# ver apenas o primeiro item da lista usa-se índices. Um índice é o número que diz onde na lista um item está. o primeiro começa com [0]
lottery = [3,43,12,30,59]
print(lottery[3])

# para apagar algum objeto da lista usa o índice e o metodo pop()
lottery = [3,43,12,30,59]
lottery.pop(3)
print(lottery)