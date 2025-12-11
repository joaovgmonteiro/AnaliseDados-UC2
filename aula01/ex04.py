import pandas as pd

s = pd.Series([10, 20, 30], index = ["a", "b", "c"], name = "Numeros")

# Seleção de valores por indice
print(s["b"])

# Seleção de multiplos valores por indice
print(s[["a", "c"]])

# Operações de filtragem
print(s[s > 15])

# Operações Aritmeticas basicas
print(s * 2)
print(s + 5)

# Suporte a variáveis nulas
s2 = pd.Series([1, None, 3])
print(s2.isnull()) # Achar valores nulos na serie
print(s2.fillna(0)) # Vai achar o nulo e irá atribuir o valor 0.

# Operações aritmeticas entre duas Séries
s1 = pd.Series([10, 20, 30], index = ["a", "b", "c"])
s2 = pd.Series([1, 2, 3], index = ["a", "b", "c"])
print(s1 + s2)