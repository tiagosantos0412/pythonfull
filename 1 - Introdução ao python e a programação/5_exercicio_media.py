#Escreva um programa onde o usuário digite duas notas e ele mostre a média das duas notas

print('Média Escolar')
nome = input('Insira o nome do aluno: ')
nota_1 = float(input('Digite a primeira nota do aluno: '))
nota_2 = float(input('Digite a segunda nota do aluno: '))
nota_3 = float(input('Digite a terceira nota do aluno: '))
nota_4 = float(input('Digite a quarta nota do aluno: '))

media = int((nota_1 + nota_2 + nota_3 + nota_4) / 4)

print(f'A média do aluno {nome} é: {media}.')