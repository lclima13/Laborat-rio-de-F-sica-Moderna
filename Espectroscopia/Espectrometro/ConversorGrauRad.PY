import math

nome_arquivo = 'LinhasEspectrais.txt'
#Converter Graus e minutos para graus
listaTheta = []
listaNome = []
listaThetaRad = []
listaFinal = []
numero = 0
while True:
  #Contador
  numero +=1
  #Nome da Linha espectral
  nome = input('Nome da Linha espectral: ')
  #Angulo em Graus e minutos
  g = float(input("grau: "))
  m = float(input("minuto: "))
  minuto = g*60+m

  #Angulo Somente em Graus
  grau = minuto/60

  #Converte para Radianos
  rad = (grau*math.pi)/180

  #Adicionar a lista para printar
  listaNome.append(nome)
  listaTheta.append(grau)
  listaThetaRad.append(rad)

  #Ver ao usuario se deseja continuar
  continuar = str(input("Deseja continuar?\n"))
  if continuar == 'n':
    break 
for i in range(numero):

  listaFinal.append(f'{listaNome[i]}: {listaTheta[i]} = {listaThetaRad[i]}')
  
with open(nome_arquivo,'w') as arquivo:
	for linha in listaFinal:
		arquivo.write(f'{linha}\n')
print(listaFinal)





