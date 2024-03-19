texto = """
Variáveis e tipos de dados
Ciclo de vida de um software
-> Receber dados
-> Armazenar dados
-> Processar dados
-> Exibir os dados processados

Tipos de dados
-> int (inteiro) = 10 -100000 100 20 0 59
-> float (decimal) =  10.5 -5022.54 3.15
-> str (string) Cadeia de caracteres = 'm' 'f' 'texto' 'exemplo 1'
-> bool (boleano) = True ou False - Verdadeiro ou Falso
"""
print(texto)

numero_inteiro = 37
numero_decimal = 3.15
cadeia_de_caracteres = 'Exemplo de um texto'
booleano = True

print(f'Numero inteiro: {numero_inteiro}', type(numero_inteiro))
print(f'Numero inteiro: {numero_decimal}', type(numero_decimal))
print(f'Numero inteiro: {cadeia_de_caracteres}', type(cadeia_de_caracteres))
print(f'Numero inteiro: {booleano}', type(booleano))