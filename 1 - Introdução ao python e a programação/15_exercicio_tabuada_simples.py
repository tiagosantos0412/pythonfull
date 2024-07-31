#Receba um número inteiro do usuário e mostre a tabuada desse número.

numero = int(input('Escolha a tabuada que deseja calcular: '))
i = 0
print(f'Ótimo!!! Vamos calcular a tabuada do {numero}')
while i <= 10:
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')
    i += 1
