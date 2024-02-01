
import csv
import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm



#Para mudar o nome nos gráficos, apert crtl H e mude do nome que esta no momento para o novo nome

# Caminho para o arquivo CSV exportado
caminho_arquivo_csv = '/home/lucaslima/Área de Trabalho/Lab de Física Moderna/Espectroscopia/RED TIDE/dados_clara.csv'

# Lista para armazenar os dados
lista_de_Ta= []
lista_de_I = []
lista_de_V = []
lista_de_VIM = []

# Abrir o arquivo CSV e ler os dados a partir da terceira linha
with open(caminho_arquivo_csv, 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    
    # Avançar até a terceira linha
    for _ in range(1):
        next(leitor_csv)
    
    # Iterar sobre as linhas restantes do arquivo CSV
    for linha in leitor_csv:
        # Assumindo que a coluna desejada é a primeira (índice 0)
        Ta = float(linha[0])
        I = float(linha[1])
        V = float(linha[2])
        VIM = float(linha[4])
        print(Ta,I,V,VIM)
        lista_de_Ta.append(Ta)
        lista_de_I.append(I)
        lista_de_V.append(V)
        lista_de_VIM.append(VIM)

# Plotar grafico da infiltração
plt.plot(lista_de_Ta,lista_de_I, color = 'blue')
plt.xlabel('Tempo Acumulado (Ta) [min]')
plt.ylabel('Infiltração (I) [cm]')
plt.title('Infiltração X Tempo Acumulado')
plt.grid()
plt.show()

# Plotar grafico da velocidade de infiltração
plt.plot(lista_de_Ta,lista_de_V, color = 'red')
plt.xlabel('Tempo Acumulado (Ta) [min]')
plt.ylabel('Velocidade  de Infiltração (VI) [cm/min]')
plt.title('Velocidade de Infiltração X Tempo Acumulado')
plt.grid()
plt.show()

# Plotar grafico da velocidade de infiltração
plt.plot(lista_de_Ta,lista_de_VIM, color = 'black')
plt.xlabel('Tempo Acumulado (Ta) [min]')
plt.ylabel('Velocidade  de Infiltração Média (VIM) [cm/min]')
plt.title('Velocidade de Infiltração Média X Tempo Acumulado')
plt.grid()
plt.show()

#Todos JUntos
plt.plot(lista_de_Ta,lista_de_I,label = 'I[cm]', color = 'blue')
plt.plot(lista_de_Ta,lista_de_V,label = 'VI[cm/min]', color = 'red')
plt.plot(lista_de_Ta,lista_de_VIM,label = 'VIM[cm/min]', color = 'black')
plt.xlabel('Tempo Acumulado [min]')
plt.ylabel('Valores')
plt.title('Relação entre os atributos I, VI e VIM')
plt.grid()
plt.legend()
plt.show()


