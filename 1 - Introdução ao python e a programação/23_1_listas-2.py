idades = [37, 25, 70, 49]

# Inserindo itens na lista com o insert
# Diferente do append que acresenta um ítem no final 
# O insert pode ser acrescentado em qualquer índice

idades.insert(0, 22) # adicionando o ítem 22 no índice 0
idades.insert(2, 58) # adicionando o ítem 58 no índice 2

print(idades)

# Remover ítens da lista com o pop
idades.pop() # removido o último numero da lista
print(idades)

# posso também informar um index existente no range da lista para ser removido
# removendo o ítem do índice 0
idades.pop(0)
print(idades)