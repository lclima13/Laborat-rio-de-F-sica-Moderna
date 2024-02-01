import csv
import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#Adicione o numero e veja o espectro:
#Hg01[1] Hg02[2] Hg03[3] LED Tubo[4] HeNe[5] Vm01[6] Vm02[7] Vm03[8] Vm04[9] CuNO3[10]
#Na01[11] Na02[12] Na03[13] Na04[14] Led_Viol_Forte[15] Led_Viol[16] Laser_verde[17] Isqueiro[18]
numero_espectro = 3

#Adicione um intervalo de sinal que deseja avaliar
antes_sinal = [440,490]
depos_sinal = [494,539]

# Caminho para o arquivo CSV exportado
caminho_arquivo_csv = '/home/lucaslima/Área de Trabalho/Lab de Física Moderna/Espectroscopia/RED TIDE/dados_RED_TIDE.csv'

# Lista para armazenar os dados
lista_de_dados = []
lista_de_lambdas = []

lista_nomes = ['Hg01', 'Hg02', 'Hg03', 'LED Tubo', 'HeNe', 'Vm01', 'Vm02', 'Vm03', 'Vm04', 'CuNO3',
            'Na01', 'Na02', 'Na03', 'Na04', 'Led_Viol_Forte', 'Led_Viol',
              'Laser_verde', 'Isqueiro']
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




#Dados do possível Sinal entre 450 e 533 nm 


# Lista de dados

dados = []
lambdas_intervalo_sinal = []
intensidade_intervalo_sinal = []
for i in lista_de_lambdas:
    i = int(i)
    print(i)
    if antes_sinal[0]<=i<=antes_sinal[1]:
        dados.append(lista_de_dados[i-380])

    elif depos_sinal[0]<=i<=depos_sinal[1]:
        dados.append(lista_de_dados[i-380])
        
    if antes_sinal[0]<=i<=depos_sinal[1]:
        lambdas_intervalo_sinal.append(float(i))
        intensidade_intervalo_sinal.append(lista_de_dados[i-380])


lista_de_dados = intensidade_intervalo_sinal
lista_de_lambdas = lambdas_intervalo_sinal
#dados = lista_de_dados
# Plotar grafico da espectroscopia
plt.plot(lista_de_lambdas,lista_de_dados)
plt.xlabel('$\lambda$(nm)')
plt.ylabel('Intensidade')
plt.title(f'Espectroscopia {lista_nomes[numero_espectro-1]} Red Tide USB 650')
plt.grid()
plt.show()

# Criar o histograma
plt.hist(dados, bins='auto', alpha=0.7, color='blue', edgecolor='black')

# Adicionar rótulos e título ao gráfico
plt.xlabel('Intensidade')
plt.ylabel('Frequência')
plt.title(f'Histograma dos Dados {lista_nomes[numero_espectro-1]}')
plt.grid()
# Mostrar o gráfico
plt.show()

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
plt.title(f'Histograma e Distribuição Gaussiana dos Dados {lista_nomes[numero_espectro-1]}')
plt.legend()
plt.grid()
plt.show()

#Plotar Distribuição Gaussiana
plt.plot(x, y, '-r', label='Distribuição Gaussiana')
plt.xlim(-1,1)
plt.legend()
plt.title(f'Distribuição Gaussiana {lista_nomes[numero_espectro-1]}')
plt.grid()
plt.show()

#Sinal e Ruido 1*sigma
limiar_ruido1 = media + 1 * desvio_padrao

cores = ['blue' if valor <= limiar_ruido1 else 'red' for valor in lista_de_dados]

plt.scatter(lista_de_lambdas, lista_de_dados, c=cores,marker='o',s = 10)

plt.ylabel('Intensidade')
plt.xlabel('$\lambda$(nm)')
plt.title(f'Gráfico Sinal/Ruido {lista_nomes[numero_espectro-1]} para 1$\sigma$(68%)')

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

plt.ylabel('Intensidade')
plt.xlabel('$\lambda$(nm)')
plt.title(f'Gráfico Sinal/Ruido {lista_nomes[numero_espectro-1]} para 2$\sigma$(95%)')

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

plt.ylabel('Intensidade')
plt.xlabel('$\lambda$(nm)')
plt.title(f'Gráfico Sinal/Ruido {lista_nomes[numero_espectro-1]} para 3$\sigma$(99,7%)')

legend_labels = ['Ruído', 'Sinal']
legend_colors = ['blue', 'red']

for label, color in zip(legend_labels, legend_colors):
    plt.scatter([], [], color=color, label=label)

plt.legend()
plt.show()


from scipy import stats


# Calcula o intervalo de confiança para a média (assumindo distribuição normal)
confidence_level = 0.95  # Nível de confiança de 95%
mean_ly = np.mean(lista_de_dados)
std_ly = np.std(lista_de_dados, ddof=1)  # Use ddof=1 para calcular a amostra padrão

# Calcula o intervalo de confiança
confidence_interval = stats.norm.interval(confidence_level, loc=mean_ly, scale=std_ly / np.sqrt(len(lista_de_dados)))

print("Média:", mean_ly)
print("Desvio Padrão:", std_ly)
print(f"Intervalo de Confiança ({confidence_level * 100}%):", confidence_interval)

# Seu dicionário
dados_estatisticos = {'Media': media, '\nDesvio Padrao': desvio_padrao,'\nIntervalo de Confiança 95%': confidence_interval}

# Converter o dicionário para uma string JSON usando json.dumps()
# Caminho do arquivo de texto
caminho_arquivo = 'dados_estatisticos_Hg03.txt'

# Abrir o arquivo no modo de escrita
with open(caminho_arquivo, 'w') as arquivo:
    # Escrever a string JSON no arquivo
    
    for chave, valor in dados_estatisticos.items():
        linha = f"{chave}: {valor}"
        arquivo.write(linha)


