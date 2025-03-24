maiorPreco = 0
nomeMP = ''
nome = ''
contador = 0
while nome != 'XXX':
    contador +=1
    nomeP = input(f'Digite o nome do produto {contador}#: ')
    valorP = int(input(f'Digite o valor do produto {contador}#'))
    if valorP > maiorPreco:
        maiorPreco = valorP
        nomeMP = nomeP
print(f'O maior preço inserido foi: {maiorPreco} no item {nomeMP}')