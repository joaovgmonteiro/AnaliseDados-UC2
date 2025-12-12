import numpy as np

dados = np.array([12, 15, 18, 20, 22, 25, 27, 30])

mediana = np.median(dados)
q1 = np.quantile(dados, 0.25)
q2 = np.quantile(dados, 0.50)
q3 = np.quantile(dados, 0.75)

print("Mediana:", mediana)
print("Q1:", q1)
print("Q2 (mediana):", q2)
print("Q3:", q3)