#entrada
meses = float(input('entre com os meses: '))
dias = float(input('entre com os dias: '))
anos = float(input('entre com os anos'))
#processamento
meses = meses * 30
anos = anos * 365
qtd_dias = meses + anos + dias
#saida
print('você viveu', qtd_dias,' dias')