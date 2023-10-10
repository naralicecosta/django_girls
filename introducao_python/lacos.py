girls = ['Nara', 'lice', 'victoria', 'ola', 'voce']

def hi(name):
       print('Ola ' + name + "!")
# tudo o que colocar dentro de uma instrução for com endentação será repetido para cada elemento da lista girls.
for name in girls:
    hi(name)
    print("próxima!")

# também pode usar o for em números usando a função range:
for i in range(1, 6):
    print(i)

