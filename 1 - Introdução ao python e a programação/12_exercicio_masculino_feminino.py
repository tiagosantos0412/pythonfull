#Receba F para feminimo e M para masculino e exbia o sexo da pessoa.

sexo = input('Digite F para feminino em M para masculino: ')

if sexo == 'M' or sexo ==  'm':
    print(f'Usuário do sexo masculino.')
elif sexo == 'F' or sexo == 'f':
    print(f'Usuária do sexo feminino.')
else:
    print('Valor inválido! Digite F para feminino em M para masculino.')