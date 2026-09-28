#entrada
cargo = input('entre com o seu cargo: ')
salario = float(input('entre com o seu salário: '))
#processamento
if cargo == 'prg de sistema':
    salario = salario * 1.30
elif cargo == 'ana de sistema':
    salario = salario*1.20
elif cargo == 'ana de banco de dados':
    salario = salario*1.10
#saida
else:
    print('seu salário não será aumentado')
print('seu salário agora é ', salario)