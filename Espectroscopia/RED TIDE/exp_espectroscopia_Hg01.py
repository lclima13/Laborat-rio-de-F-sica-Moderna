import csv
import matplotlib.pyplot as plt
import json

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
        dado = float(linha[1])
        lista_de_dados.append(dado)
        dado2 = float(linha[0])
        lista_de_lambdas.append(dado2)


# Exibir a listas
print(lista_de_lambdas)
print(lista_de_dados)


# Plotar grafico da espectroscopia
plt.plot(lista_de_lambdas,lista_de_dados)
plt.xlabel('$\lambda$(m)')
plt.ylabel('Intensidade')
plt.show()

# Criar o histograma
plt.hist(lista_de_dados, bins='auto', alpha=0.7, color='blue', edgecolor='black')

# Adicionar rótulos e título ao gráfico
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.title('Histograma dos Dados Hg 01')

# Mostrar o gráfico
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Lista de dados
'''
dados = []
for i in lista_de_dados:
    if i<=0.3:
        dados.append(i)
'''

dados = lista_de_dados

# Calcular média e desvio padrão
media = np.mean(dados)
desvio_padrao = np.std(dados)

# Imprimir média e desvio padrão
print(f'Média: {media}')
print(f'Desvio Padrão: {desvio_padrao}')

# Construir a distribuição gaussiana
xmin, xmax = min(dados) - 1, max(dados) + 1
x = np.linspace(xmin, xmax, 100)
y = norm.pdf(x, media, desvio_padrao)

# Plotar o histograma dos dados
plt.hist(dados, bins='auto', density=True, alpha=0.7, color='blue', edgecolor='black')

# Plotar a distribuição gaussiana
plt.plot(x, y, '-r', label='Distribuição Gaussiana')

# Adicionar rótulos e título ao gráfico
plt.xlabel('Valores')
plt.ylabel('Densidade de Probabilidade')
plt.title('Histograma e Distribuição Gaussiana dos Dados')

# Adicionar legenda
plt.legend()

# Mostrar o gráfico
plt.show()

plt.plot(x, y, '-r', label='Distribuição Gaussiana')
plt.xlim(-1,1)

plt.legend()
plt.show()


#Z-dispersão
lista_z = []
for i in lista_de_dados:
    z = (i-media)/desvio_padrao
    lista_z.append(z)

plt.plot(lista_de_lambdas,lista_z)
plt.xlabel('$\lambda$(m)')
plt.ylabel('Z-Dispersão')
plt.show()




# Seu dicionário
dados_estatisticos = {'Media': media, 'Desvio Padrao': desvio_padrao}

# Converter o dicionário para uma string JSON usando json.dumps()
dicionario_json = json.dumps(dados_estatisticos)

# Caminho do arquivo de texto
caminho_arquivo = 'dados_estatisticos_Hg01.txt'

# Abrir o arquivo no modo de escrita
with open(caminho_arquivo, 'w') as arquivo:
    # Escrever a string JSON no arquivo
    arquivo.write(dicionario_json)
