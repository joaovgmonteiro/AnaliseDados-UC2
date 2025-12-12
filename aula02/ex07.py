import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Nome": ["Ana", "Bruno", "Carlos"],
    "Idade": [23, 30, 27],
    "Cidade": ["Rio", "São Paulo", "Belo Horizonte"]
}

df = pd.DataFrame(dados)

print("\nEstatísticas rápidas\n")
print("Média das idades:", df["Idade"].mean())
print(df.describe())  # resumo estatístico

print("\nIntegração com gráficos\n")

df["Idade"].plot(kind="bar", title="Idade dos participantes") # Gera um grafico de barras.
plt.show()
