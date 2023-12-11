import csv
import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

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



# Plotar grafico da espectroscopia
plt.plot(lista_de_lambdas,lista_de_dados)
plt.xlabel('$\lambda$(nm)')
plt.ylabel('Intensidade')
plt.grid()
plt.show()

# Criar o histograma
plt.hist(lista_de_dados, bins='auto', alpha=0.7, color='blue', edgecolor='black')

# Adicionar rótulos e título ao gráfico
plt.xlabel('Intensidade')
plt.ylabel('Frequência')
plt.title('Histograma dos Dados Hg 01')
plt.grid()
# Mostrar o gráfico
plt.show()



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


plt.hist(dados, bins='auto', density=True, alpha=0.7, color='blue', edgecolor='black')# Plotar o histograma dos dados


plt.plot(x, y, '-r', label='Distribuição Gaussiana')# Plotar a distribuição gaussiana
plt.xlabel('Intensidade')
plt.ylabel('Densidade de Probabilidade')
plt.title('Histograma e Distribuição Gaussiana dos Dados')
plt.legend()
plt.grid()
plt.show()

#Plotar Distribuição Gaussiana
plt.plot(x, y, '-r', label='Distribuição Gaussiana')
plt.xlim(-1,1)
plt.legend()
plt.grid()
plt.show()

#Sinal e Ruido 1*sigma
limiar_ruido1 = media + 1 * desvio_padrao

cores = ['blue' if valor <= limiar_ruido1 else 'red' for valor in lista_de_dados]

plt.scatter(lista_de_lambdas, lista_de_dados, c=cores,marker='o',s = 10)

plt.xlabel('Intensidade')
plt.ylabel('$\lambda$(nm)')
plt.title('Gráfico Sinal/Ruido para 1$\sigma$(68%)')

legend_labels = ['Ruído', 'Sinal']
legend_colors = ['blue', 'red']

for label, color in zip(legend_labels, legend_colors):
    plt.scatter([], [], color=color, label=label)

plt.legend()
plt.grid()
plt.show()

#Sinal e ruido 2 sigmas
limiar_ruido2 = media + 2 * desvio_padrao

cores = ['blue' if valor <= limiar_ruido2 else 'red' for valor in lista_de_dados]

plt.scatter(lista_de_lambdas, lista_de_dados, c=cores,marker='o',s = 10)

plt.xlabel('Intensidade')
plt.ylabel('$\lambda$(nm)')
plt.title('Gráfico Sinal/Ruido para 2$\sigma$(95%)')

legend_labels = ['Ruído', 'Sinal']
legend_colors = ['blue', 'red']

for label, color in zip(legend_labels, legend_colors):
    plt.scatter([], [], color=color, label=label)

plt.legend()
plt.grid()
plt.show()

#Sinal e ruido 3 sigmas
limiar_ruido3 = media + 3 * desvio_padrao

cores = ['blue' if valor <= limiar_ruido3 else 'red' for valor in lista_de_dados]

plt.scatter(lista_de_lambdas, lista_de_dados, c=cores,marker='o',s = 10)

plt.xlabel('Intensidade')
plt.ylabel('$\lambda$(nm)')
plt.title('Gráfico Sinal/Ruido para 2$\sigma$(99,7%)')

legend_labels = ['Ruído', 'Sinal']
legend_colors = ['blue', 'red']

for label, color in zip(legend_labels, legend_colors):
    plt.scatter([], [], color=color, label=label)

plt.legend()
plt.show()

# Seu dicionário
dados_estatisticos = {'Media': media, '\nDesvio Padrao': desvio_padrao}

# Converter o dicionário para uma string JSON usando json.dumps()
# Caminho do arquivo de texto
caminho_arquivo = 'dados_estatisticos_Hg01.txt'

# Abrir o arquivo no modo de escrita
with open(caminho_arquivo, 'w') as arquivo:
    # Escrever a string JSON no arquivo
    
    for chave, valor in dados_estatisticos.items():
        linha = f"{chave}: {valor}"
        arquivo.write(linha)