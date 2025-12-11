import pandas as pd

# Lendo a planilha
df = pd.read_excel("turma_alunos.xlsx")

# Estatisticas basicas
print("Idade - Média:", df["Idade"].mean())
print("Idade - Máxima: ", df["Idade"].max())
print("Idade - Mínima: ", df["Idade"].min())

print("\nNota - Média:", df["Nota"].mean())
print("Nota - Máxima:", df["Nota"].max())
print("Nota - Mínima:", df["Nota"].min())

print("\nFrequência - Somatório:", df["Frequência (%)"].sum())
print("Frequência - Média:", df["Frequência (%)"].mean())

# Distribuição por Curso
print(df["Curso"].value_counts())

# Distribuição por Sexo
print(df["Sexo"].value_counts())
