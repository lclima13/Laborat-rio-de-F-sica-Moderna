import csv
import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#Adicione o numero e veja o espectro:
#Hg01[1] Hg02[2] Hg03[3] LED Tubo[4] HeNe[5] Vm01[6] Vm02[7] Vm03[8] Vm04[9] CuNO3[10]
#Na01[11] Na02[12] Na03[13] Na04[14] Led_Viol_Forte[15] Led_Viol[16] Laser_verde[17] Isqueiro[18]

numero_espectro = 18

#Para mudar o nome nos gráficos, apert crtl H e mude do nome que esta no momento para o novo nome
lista_nomes = ['Hg01', 'Hg02', 'Hg03', 'LED Tubo', 'HeNe', 'Vm01', 'Vm02', 'Vm03', 'Vm04', 'CuNO3',
            'Na01', 'Na02', 'Na03', 'Na04', 'Led_Viol_Forte', 'Led_Viol',
              'Laser_verde', 'Isqueiro']

# Caminho para o arquivo CSV exportado
caminho_arquivo_csv = '/home/lucaslima/Área de Trabalho/Lab de Física Moderna/Espectroscopia/RED TIDE/dados_RED_TIDE.csv'

# Lista para armazenar os dados
lista_de_dados = []
lista_de_lambdas = []

# Abrir o arquivo CSV e ler os dados a partir da terceira linha
with open(caminho_arquivo_csv, 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    
    # Avançar até a terceira linha
    for _ in range(2):
        next(leitor_csv)
    
    # Iterar sobre as linhas restantes do arquivo CSV
    for linha in leitor_csv:
        # Assumindo que a coluna desejada é a primeira (índice 0)
        dado = float(linha[numero_espectro])
        lista_de_dados.append(dado)
        dado2 = float(linha[0])
        lista_de_lambdas.append(dado2)

# Plotar grafico da espectroscopia
plt.plot(lista_de_lambdas,lista_de_dados)
plt.xlabel('$\lambda$(nm)')
plt.ylabel('Intensidade')
plt.title(f'Espectroscopia {lista_nomes[numero_espectro-1]} Red Tide USB 650')
plt.grid()
plt.show()