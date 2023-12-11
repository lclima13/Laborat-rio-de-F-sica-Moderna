from scipy.stats import ttest_ind, shapiro
import matplotlib.pyplot as plt

# Exemplo de dados (substitua essas listas pelos seus dados reais)
sinais = [10, 12, 11, 13, 15, 14, 12, 11, 13, 10]
ruidos = [5, 7, 6, 8, 9, 7, 8, 6, 5, 7]

# Visualização inicial (opcional)
plt.hist(sinais, alpha=0.5, label='Sinais')
plt.hist(ruidos, alpha=0.5, label='Ruídos')
plt.legend()
plt.show()

# Teste de Normalidade
_, p_valor_sinais = shapiro(sinais)
_, p_valor_ruidos = shapiro(ruidos)

if p_valor_sinais > 0.05 and p_valor_ruidos > 0.05:
    print("Ambas as amostras seguem uma distribuição normal.")
else:
    print("Pode ser necessário considerar testes não paramétricos.")

# Teste t para Amostras Independentes
estatistica_t, p_valor_t = ttest_ind(sinais, ruidos)

print("Estatística t:", estatistica_t)
print("Valor p:", p_valor_t)

# Interpretação do Resultado
nivel_significancia = 0.05

if p_valor_t < nivel_significancia:
    print("Rejeitamos a hipótese nula. Há uma diferença significativa entre sinais e ruídos.")
else:
    print("Não há evidências suficientes para rejeitar a hipótese nula. Não há diferença significativa.")
