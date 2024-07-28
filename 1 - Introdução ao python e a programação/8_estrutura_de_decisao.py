# if else elif
nome_do_aluno = 'Tiago Felipe dos Santos'
media_escolar = 8

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

