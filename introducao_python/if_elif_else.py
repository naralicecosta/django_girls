if 3 > 2:
    print("3 é maior que dois!")
else:
    print(" não é maior que 2")

name = "Nara"
if name == "Ola":
    print('Ola Ola')
elif name == 'Nara':
    print("Ola Nara")
else:
    print('Ola estranho')


# o elif possibilita adicionar uma condição que so vai ser executada se a primeira condição for falsa

volume = 45
if volume < 20: 
    print("Está um pouco baixo")
elif 20 <= volume < 40: 
    print("Está bom para música ambiente")
elif 40 <= volume < 60: 
    print("Perfeito, posso ouvir todos os detalhes")
elif 60 <= volume < 80: 
    print("Ótimo para festas!")
elif 80 <= volume < 100: 
    print("Está muito alto!")
else: 
    print("Meus ouvidos doem! :(")