import math
listaRad = []
listaGrau = []
contador = 0
while True:
	g = float(input('Digite o grau: '))
	m = float(input('Digite o minuto: '))

	grau = (g*60+m)/60
	rad = (math.pi*((g*60+m))/60)/180

	print(grau, rad)
	contador += 1
	listaRad.append(str(rad))
	listaGrau.append(str(grau))
	if contador == 7:
		break
with open('angulos.txt','w') as arquivo:
	for linha in listaRad:
		arquivo.write(f'{linha}\n')
	for linha in listaGrau:
		arquivo.write(f'{linha}\n')
