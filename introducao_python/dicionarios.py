# criando um dicionario
participant = {'name' : 'Nara', 'country': 'Natal/RN', 'favorite_numbers': [7,42,92]}
# para verificar o conteúdo de chaves individuais com a sintaxe:
print(participant['name'])

#alterando a lista do dicionário
participant['favorite_language'] = 'Python'
print(participant)

#numero de pares chave-valor que ele contém
print(len(participant))

#deletar um item do dicionário / pop()
participant.pop('favorite_numbers')
[7,42,92]
print(participant)

#mudar um valor
participant['country'] = 'Germany'
print(participant)