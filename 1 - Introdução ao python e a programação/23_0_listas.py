nomes = ['Tiago', 'Viviane', 'Raul']

# Retorna o tipo do dado 
print(type(nomes))
# Imprime toda a lista
print(nomes)
# Retorna o tamanho da lista
print(f'Tamanho da lista:  {len(nomes)}')
# Alterando o valor do índice 0 de uma lista
nomes[0] = 'Tiago Felipe'
print(nomes)
# Adicionar elementos na lista
nomes.append('Helena')
print(nomes)

usuarios = []
contador = 0
while True:
    usuario = input('Digite 0 para sair ou cadastre um novo usuário...:  ')
    if usuario == "0":
        break
    else:
        usuarios.append(usuario)
    contador += 1    
print(f'Fim do cadastro, você cadastrou {contador} novos usuarios:')
print(usuarios)