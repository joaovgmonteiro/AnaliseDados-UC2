# Cenário 01: Controle de vendas em uma loja

import pandas as pd

vendas = pd.Series([2500, 3200, 1800, 4000, 3700, 2900, 3100], 
                   index= ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"],
                   name= "Vendas da semana")

print(vendas)

print("\n1) Vendas de quarta-feira: ", vendas["Qua"])
print("2) Vendas de sexta e sábado:\n", vendas[["Sex", "Sab"]])
print("3) Dias com vendas acima de 3000:\n", vendas[vendas > 3000])
print("4) Total da semana:", sum(vendas))
'''
variacao = vendas.pct_change() # Descobre a variação entre o numero atual com o anterior. Cria uma lista com a comparação
print(variacao)
filtro_10 = variacao >= 0.10 # Cria uma serie mostrando True e false quais atendem ao filtro
print(filtro_10)
vendas_com_aumento = vendas[filtro_10] # Sobrepoe as duas listas. Uma com os V e F e a outra com os numeros. E descobre qual a atende ao filtro

'''



print("5) Vendas com aumento de 10%:\n", vendas * 1.10) # Aumenta 10% do valor de cada valor.