#Defina um usuário e senha e depois verifique se 
#login do usuário é valido.

tentativas = 1
_usuario = 'tiagosantos0412'
_senha = '123456'
_nome = 'Tiago Felipe dos Santos'

bloqueado = False
logado = False

while tentativas <= 3:
    usuario = input('Usuário...: ')
    senha = input('Senha.......: ')
    
    if usuario == _usuario and senha == _senha:
        print(f'Bem-vindo {_nome}')
        logado = True
        break
    else:
        print('Login inválido!')
        print('Após a 3ª tentativa seu usuário será bloqueado!')
        print(f'Tentativas restantes: {3 - tentativas}')
        logado = False
    
    tentativas += 1

if not logado:
    bloqueado = True
    print('Usuário bloqueado após 3 tentativas erradas.')
