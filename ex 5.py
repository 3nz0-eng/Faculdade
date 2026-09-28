#entrada
usuario = input('entre com o nome usuário: ')
senha = input('entre com a senha: ')
#processamento
if (usuario == 'procopio' and senha == '12345') or (usuario == 'paiva' and senha == '54321') :
#saida
    print('acesso liberado')
else:
    print('acesso negado')