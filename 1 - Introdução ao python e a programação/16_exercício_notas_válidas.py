#Escreva um programa que receba notas de um aluno (0 - 10), caso
#a nota digitada esteja fora dessa intervalo peça para o professor digitar
#novamente.

controlador = True
contador = 0
notas = []


while controlador:
    nota_digitada = int(input('Digite a nota:'))
    if nota_digitada < 0 or nota_digitada > 10:
        print('Erro no intervalo de notas!\nDigite as notas entre 0 e 10!')
    else:
        notas.append(nota_digitada)
        contador += 1
    if contador >= 4:
        controlador = False
    
print(f'Notas registradas.....: {notas}')