#Receba 3 números inteiros e exiba o maior deles.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

if n1 > n2 and n2 > n3:
    print(f'O número maior foi N1 com o valor: {n1}')
elif n1 < n2 and n2 > n3:
    print(f'O número maior foi N2 com o valor: {n2}')
else:
    print(f'O número maior foi N3 com o valor: {n3}')