# Dataframes

import pandas as pd

dados = {
    "Nome": ["Ana", "Bruno", "Carlos"],
    "Idade": [23, 35, 29],
    "Cidade": ["Rio", "São Paulo", "Belo Horizonte"]
}

df = pd.DataFrame(dados)


print("\nSelecionar apenas a coluna ""Nome""\n")
print(df["Nome"])

print("\nFiltrar pessoas com idade maior que 25\n")
print(df[df["Idade"] > 25])