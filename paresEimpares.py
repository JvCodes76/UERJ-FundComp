qtdPares = 0
qtdImp = 0
mediaPares = 0
numero = 1
while numero != 0:
    numero = int(input('insira um numero, insira 0 para parar: '))
    if numero%2 == 1:
        qtdImp+=1
    else:
        qtdPares+=1
        mediaPares+=numero
mediaPares/=(qtdPares-1)
print(f'Foram inseridos {qtdImp} numeros impares')
print(f'Foram inseridos {qtdPares} numeros pares')
print(f'A média dos numeros pares inseridos foi: {mediaPares}')
