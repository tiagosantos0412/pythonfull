#Receba 4 notas de um aluno e exiba se ele foi aprovado (nota maior ou igual que 6)
#se ele ficou de recuperação (nota maior ou igual a 4) ou se ele foi
#reprovado (nota menor do que 4)

print('Média Escolar')
nome_do_aluno = input('Insira o nome do aluno: ')
nota_1 = float(input('Digite a primeira nota do aluno: '))
nota_2 = float(input('Digite a segunda nota do aluno: '))
nota_3 = float(input('Digite a terceira nota do aluno: '))
nota_4 = float(input('Digite a quarta nota do aluno: '))

media_escolar = int((nota_1 + nota_2 + nota_3 + nota_4) / 4)

if media_escolar >= 10:
    print(f'Parabéns {nome_do_aluno}, você foi aprovado com a nota máxima!')
    print(f'Sua média foi {media_escolar}')
elif media_escolar >=7 and media_escolar < 10:
    print(f'Parabéns {nome_do_aluno}, você foi aprovado.')
    print(f'Sua média foi {media_escolar}')
elif media_escolar < 7 and media_escolar >= 5:
    print(f'Atenção {nome_do_aluno}, você está de recuperação!.')
    print(f'Sua média foi {media_escolar}')
else:
    print(f'Lamento informar {nome_do_aluno}, você foi reprovado.')
    print(f'Sua média foi {media_escolar}')

