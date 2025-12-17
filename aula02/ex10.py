import numpy as np
import pandas as pd 

# Dados de exemplo
df = pd.read_excel('aula002_cenario_quartil.xlsx') # Esse comando ja me retorna um dataframe
print(df, "\n")
#df = pd.DataFrame(dados) # Utilizar essa linha de comando seria redundante.
#print(df, "\n")

dados_array = np.array(df["Nota de Satisfação"])
print(dados_array, "\n")

# Calcular quartis
q1 = np.percentile(dados_array, 25) # 1º quartil representa 25% do todo
q2 = np.percentile(dados_array, 50) # Mediana é o mesmo que o quartil 50
q3 = np.percentile(dados_array, 75) #3º quartil representa 75% do todo

# Exibir quartis
print(f"Primeiro quartil (Q1): {q1}")
print(f"Segundo quartil (Q2, Mediana): {q2}")
print(f"Terceiro quartil (Q3): {q3}")

