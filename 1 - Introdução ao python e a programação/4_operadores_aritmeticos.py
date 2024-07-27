# + - * / ** % // math.sqrt ()

import math

numero_1 = int(input('Digite o numero 1: '))
numero_2 = int(input('Digite o numero 2: '))

print(f'Soma -> Numero 1 + Numero 2 = {numero_1 + numero_2}')
print(f'Subtração -> Numero 1 - Numero 2 = {numero_1 - numero_2}')
print(f'Multiplicação -> Numero 1 * Numero 2 = {numero_1 * numero_2}')
print(f'Divisão -> Numero 1 / Numero 2 = {numero_1 / numero_2}')
print(f'Divisão por inteiro -> Numero 1 // Numero 2 = {numero_1 // numero_2}')
print(f'Exponenciação -> Numero 1 ** Numero 2 = {numero_1 ** numero_2}')
print(f'Módulo ou resto da divisão -> Numero 1 % Numero 2 = {numero_1 % numero_2}')
print(f'Raiz quadrada de ->  {numero_1} = {math.sqrt(numero_1)}')
print(f'Raiz quadrada de ->  {numero_2} = {math.sqrt(numero_2)}')

# Precedência de operações (Prioridades)
# 0 - Alterando as prioridades insira ()
# 1- Raiz quadrada e Exponenciação
# 2 - Multiplicação e Divisão
# 3 - Adicição e Subtração
