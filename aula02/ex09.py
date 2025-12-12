import numpy as np

# Dados de exemplo
dados = np.array([12, 15, 17, 20, 22, 25, 28, 30, 35, 40])
print(dados,"\n")

# Calcular quartis
q1 = np.percentile(dados, 25) # 1º quartil representa 25% do todo
q2 = np.percentile(dados, 50) # Mediana é o mesmo que o quartil 50
q3 = np.percentile(dados, 75) #3º quartil representa 75% do todo

# Exibir quartis
print(f"Primeiro quartil (Q1): {q1}")
print(f"Segundo quartil (Q2, Mediana): {q2}")
print(f"Terceiro quartil (Q3): {q3}")
