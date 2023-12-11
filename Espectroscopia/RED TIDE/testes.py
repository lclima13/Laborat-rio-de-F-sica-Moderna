import matplotlib.pyplot as plt

# Lista de dados
ly = [1, 1, 1, 0, 2, 1, 1, 2, 3, 4, 1, 1, 1, 3, 1]

# Cores para os pontos
cores = ['blue' if valor <= 1 else 'red' for valor in ly]

# Criar o gráfico de pontos
plt.scatter(range(len(ly)), ly, c=cores,marker='o',linestyle='-')

# Adicionar rótulos e título
plt.xlabel('Índice')
plt.ylabel('Valores')
plt.title('Gráfico de Pontos com Cores Diferentes')

# Exibir o gráfico
plt.show()


