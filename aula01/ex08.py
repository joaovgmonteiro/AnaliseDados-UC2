# Dataframes

import pandas as pd

dados = {
    "Nome": ["Ana", "Bruno", "Carlos"],
    "Idade": [23, 35, 29],
    "Cidade": ["Rio", "São Paulo", "Belo Horizonte"]
}

df = pd.DataFrame(dados)
print(df)