import pandas as pd

dados = {
    "Nome": ["Ana", "Bruno", "Carlos"],
    "Idade": [23, 30, 27],
    "Cidade": ["Rio", "São Paulo", "Belo Horizonte"]
}

df = pd.DataFrame(dados)

print("\nAdicionar uma nova coluna calculada\n")
df["AnoNascimento"] = 2025 - df["Idade"] # Criação de uma nova coluna
print(df)

print("\nOrdenar os dados pela idade\n")
print(df.sort_values("Idade"))