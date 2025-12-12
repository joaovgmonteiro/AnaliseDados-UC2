# Série com Pandas - Cenário 03: Batimentos entre Estoque
import pandas as pd

estoque_A = pd.Series([100, 200, 150], index= ["Produto1", "Produto2", "Produto3"])
estoque_B = pd.Series([80, 220, 130], index= ["Produto1", "Produto2", "Produto3"])

print("Filial A:\n", estoque_A)
print("Filial B:\n", estoque_B)

total_estoque = estoque_A + estoque_B
diferenca_estoque = estoque_A - estoque_B

print("\n1) Soma dos estoques:\n", total_estoque)
print("2) Produtos com mais de 300 unidades:\n", total_estoque[total_estoque > 300])
print("3) Diferença de estoque entre filiais:\n", abs(diferenca_estoque ))