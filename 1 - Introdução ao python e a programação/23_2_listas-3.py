produto = ['Notebook', 'Monitor LG', 'Teclado Logitec', 'Processo Risen', 'Adaptador USB']
# Descobrindo o index de um elemnto de uma lista
indice = produto.index('Teclado Logitec')
print(f'O índice do produto Teclado LOgitec é: {indice}')

# Podemos utilizar o método sort para ordenar uma lista
# o comando sort altera a lista original
produto.sort() # ordenando os ítens em ordem alfabética
print(produto)

numeros = [5, 12, 7, 1, 9, 3]
numeros.sort() #ordenando os números em ordem crescente
print(numeros)

numeros.sort(reverse=True) #ordenando os números em ordem decrescente
print(numeros)

# Se não quisermos alterar a lista original, podemos utilizar
# o método sorted, que faz uma cópia da lista original e altera apenas a cópia.
print(sorted(numeros))
# Podemos também armazenas esta cópia da lista em uma nova variável
numeros_ordenados = sorted(numeros)
print(numeros_ordenados)

