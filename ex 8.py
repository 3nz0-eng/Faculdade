#entrada
horas_valor = float(input('entre com o valor das horas: '))
qtd_horas = float(input('entre com a quantidade de horas trabalhadas: '))
#processamento
salario_b = horas_valor * qtd_horas
ir = 0
mensagem = '0'
if salario_b <= 0:
    print('número inválido')
else:
    if salario_b <= 900:
        ir = 0
        mensagem = 'isento'
    elif salario_b > 900 and salario_b <= 1500:
        ir = 0.05
        mensagem = '5%'
    elif salario_b > 1500 and salario_b <= 2500:
        ir = 0.1
        mensagem = '10%'
    elif salario_b > 2500:
        ir = 0.2
        mensagem = '20%'
inss = 0.1
salario_l = salario_b - (salario_b * ir)  - (salario_b * inss)
#saida
print('salário bruto: ',salario_b)
print('(-)IR(',mensagem,'): ',salario_b * ir)
print('(-) INSS (10%): ', salario_b * inss)
print('FGTS (11%): ',salario_b * 0.11)
print('Total de descontos: ',(salario_b * ir)  + (salario_b * inss))
print('Salário Liquido: ',salario_l)