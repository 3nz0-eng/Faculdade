#entrada
peso = float(input('entre com o seu peso: '))
altura = float(input('entre com a sua altura '))
#processamento
imc = peso/altura**2
#saída
if imc < 18.5:
    print('abaixo do peso, seu imc é ', round(imc,2))
elif imc > 18.5 and imc < 25:
    print('peso normal, seu imc é ', round(imc,2))
elif imc > 25 and imc < 30:
    print('sobrepeso, seu imc é ', round(imc,2))
elif imc > 30 and imc < 35:
    print('obesidade grau1, seu imc é ', round(imc,2))
elif imc > 35 and imc < 40:
    print('obesidade grau2, seu imc é ', round(imc,2))
elif imc > 40:
    print('obesidade grau3, seu imc é ', round(imc,2))