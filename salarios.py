mediaSalF = 0
mediaSalM = 0
maiorSal30 = 0
contador = 0
contadorF = 0
contadorM = 0
idade = 1
running = True
while running:
    idade = int(input(f'Digite a idade do funcionário {contador+1}#: '))
    if idade > 0:
        contador+=1
        salario = int(input(f'Digite o salário do funcionário {contador}#: '))
        sexo = input(f'Digite o sexo do funcionário {contador}#: ')
        if int(idade) < 30:
            if maiorSal30 < salario:
                maiorSal30 = salario
        if sexo.lower() == 'f':
            mediaSalF+= salario
            contadorF+=1
        else:
            contadorM+=1
            mediaSalM+= salario
    else:
        running = False


mediaSalF/=contadorF
mediaSalM/=contadorM
print(f'O maior salário de um funcionário de até 30 anos foi: {maiorSal30}')
print(f'A média dos salários das funcionárias foi de: {mediaSalF}')
print(f'A média dos salários dos funcionários foi de: {mediaSalM}')   
                
        