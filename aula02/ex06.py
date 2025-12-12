
import pandas as pd

dados = {
    "Nome": ["Ana", "Bruno", "Carlos"],
    "Idade": [23, 30, 27],
    "Cidade": ["Rio", "São Paulo", "Belo Horizonte"]
}

df = pd.DataFrame(dados)

print("\nDefinir a coluna ""Nome"" como índice \n")
df_indexado = df.set_index("Nome")
print(df_indexado)

print("\nAcessar dados pelo índice \n")
print(df_indexado.loc["Ana"])