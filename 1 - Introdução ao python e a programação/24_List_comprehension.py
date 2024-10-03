x = [i for i in range(0, 10)]

print(x)

nomes = [input('Digite um nome...: ') for i in range(0, 3)]
print(nomes)

y = [[j for j in range(3, 7)] for i in range(0, 3)]
print(y)

k = [i for i in range(0, 11) if i > 4]
print(k)

#Referência para endereço de memória
lista1 = [1, 2, 3]
lista2 = lista1
lista3 = lista1.copy()

print(hex(id(lista1)))
print(hex(id(lista2)))
print(hex(id(lista3)))