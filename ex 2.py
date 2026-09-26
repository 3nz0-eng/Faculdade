#entrada
pi=3.14
raio = float(input('entre com o raio da base: '))
altura = float(input('entre com a altura do cilindro: '))
#processamento
base = pi * raio**2
volume = base* altura
lado_cilindro = 2*pi*raio*altura
area_total = base*2 + lado_cilindro
#saída 
print('o volume do silindro é igual a',volume)
print('a area da lateral do cilindro é igual a', lado_cilindro)
print('a area da base do cilindro é igual a', base)
print(' a area total do do cilindro é igual a ', area_total)