termoN = int(input('Primeiro termo da P.A.: '))
razao = int(input('Razão da P.A.:'))
n = int(input('Quantos termos deseja? '))
contador = 1
print(f'O {contador}# termo é: {termoN}')
while contador != n:
    termoN+=razao
    contador+=1
    print(f'O {contador}# termo é: {termoN}')
