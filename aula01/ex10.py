'''
Dataframe com Pandas - Cenário:
Imagine que você é analista de dados em uma empresa de
e-commerce. Sua tarefa é analisar o desempenho das vendas de
produtos ao longo de 2025.

A base contém mais de 1000 linhas, cada uma representando uma
venda.

Resultados Esperados
• Valor total de vendas: ?
• Média de valor por pedido: ?
• Categoria mais lucrativa: ?
• Região com maior volume de vendas: ?
• Produto mais vendido: ?

'''

import pandas as pd

df = pd.read_excel("vendas_ecommerce.xlsx")

print(f"Valor total de vendas: R$ {df["TotalValue"].sum()}")
print(f"Média de valor por pedido: R$ {df["TotalValue"].mean()}")

vendas_categoria = df.groupby("Category")["TotalValue"].sum()
print(f"Categoria mais lucrativa: {vendas_categoria.idxmax()} | Valor: R$ {vendas_categoria.max()}")

regiao_mais_vendas = df.groupby("Region")["OrderID"].count()
print(f"Região com maior volume de vendas: {regiao_mais_vendas.idxmax()} | Total pedidos na região: {regiao_mais_vendas.max()}")

produtos_vendas = df.groupby("Product")["Quantity"].sum()
print(f"Produto mais vendido: {produtos_vendas.idxmax()} | Total vendidos: {produtos_vendas.max()}")
