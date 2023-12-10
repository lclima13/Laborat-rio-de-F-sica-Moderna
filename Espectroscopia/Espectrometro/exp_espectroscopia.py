import numpy as np
import csv
from turtle import color
import matplotlib.pyplot as plt
import math
import pandas as pd
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score



#Valor de d da rede de difração
d = 1e-6

#Valores de Lambda para cada cor do banco de dados NIST
lista_lambda_NIST = [404.65650e-9,407.78370e-9,434.3634e-9,491.6068e-9,540.480e-9,567.581e-9,576.96100e-9]

#Angulos obtidos no experimento para cada linha espectral e seus erros
lista_angulos = [23.983,24.017,25.750,29.433,32.950,35,35.133]
erro_angulos = 0.02

# lista para armazenar angulos convertidos para radianos e seu erro propagado
lista_rad = []
erro_rad = (math.pi*erro_angulos)/180

#Lista para armazenar valores de lambda obtidos dos angulos e seus respectivos erros propagados
lista_erro_lambda = []
lista_lamda = []

#Calcular os valores dos angulos em rad
for i in lista_angulos:
    lista_rad.append((math.pi*i)/180)

#Calcular valores de lambda
for j in lista_rad:
    lamda = d*math.sin(j)
    lista_lamda.append(lamda)
    
#Calcular erro propagado de cada lambda
for k in lista_rad:
    lista_erro_lambda.append(math.sqrt((d*math.cos(k)*erro_rad)**2))



#Armazenar dados
titulos = ['Lambda Nist','Lambda Exp', 'Angulos(Graus)','Angulos(rad)','Erro Lambda(exp)']
nomeArquivo = 'dados_espectrospocia.csv'

# Transpor as listas
listas_transpostas = list(map(list, zip(lista_lambda_NIST, lista_lamda, lista_angulos, lista_rad, lista_erro_lambda)))

# Abre o arquivo CSV para escrita
with open(nomeArquivo, 'w', newline='') as arquivo_csv:
    # Cria um objeto escritor CSV
    escritor_csv = csv.writer(arquivo_csv)

    # Escreve os títulos das colunas
    escritor_csv.writerow(titulos)

    # Escreve as listas transpostas como linhas no arquivo CSV
    escritor_csv.writerows(listas_transpostas)

#Regressão Linear
x = np.array(lista_lambda_NIST).reshape(-1,1)
y = np.array(lista_lamda)
modelo = LinearRegression()
modelo.fit(x,y)
a_coef = modelo.coef_
l_coef = modelo.intercept_

#R²
r_quadrado = r2_score(y,modelo.predict(x))

print(a_coef)
print(l_coef)
print(r_quadrado)

#Construir gráfico
plt.errorbar(lista_lambda_NIST,lista_lamda,yerr = lista_erro_lambda, fmt = 'o',capsize = 1, color = 'black')
plt.plot(lista_lambda_NIST, l_coef+a_coef*(lista_lambda_NIST),color='red',label = f'Fit Linear(Y=aX+b)\na = {a_coef[0]}\nb = {l_coef}')
plt.xlabel('Comprimento de Onda Hg NIST (m)')
plt.ylabel('Comprimento de Onda Hg Experimento (m)')
plt.grid()
plt.legend()
plt.show()
