import mysql.connector

# Conexão com o banco de dados MySQL
conn = mysql.connector.connect(
    host="localhost",        # endereço do servidor MySQL
    user="analista_dados",      # usuário do banco
    password="Pa$$w0rd",    # senha do banco
    database="ecommerce" #,  # nome do banco de dados
    #auth_plugin='mysql_native_password'
)

cursor = conn.cursor()

# 1. Listar todas as vendas
cursor.execute("SELECT * FROM vendas_ecommerce;")
for row in cursor.fetchall():
    print(row)

# 2. Vendas realizadas na região Sudeste
cursor.execute("""
    SELECT OrderID, Product, TotalValue
    FROM vendas_ecommerce
    WHERE Region = 'Sudeste';
""")
for row in cursor.fetchall():
    print(row)

# 3. Produtos da categoria Moda
cursor.execute("""
    SELECT Product, Category, TotalValue
    FROM vendas_ecommerce
    WHERE Category = 'Moda';
""")
for row in cursor.fetchall():
    print(row)

# 4. Vendas acima de R$ 5000
cursor.execute("""
    SELECT OrderID, Product, TotalValue
    FROM vendas_ecommerce
    WHERE TotalValue > 5000;
""")
for row in cursor.fetchall():
    print(row)

# 5. Total de vendas por produto
cursor.execute("""
    SELECT Product, SUM(TotalValue) AS TotalPorProduto
    FROM vendas_ecommerce
    GROUP BY Product
    ORDER BY TotalPorProduto DESC;
""")
for row in cursor.fetchall():
    print(row)

# 6. Quantidade vendida por categoria
cursor.execute("""
    SELECT Category, SUM(Quantity) AS TotalQuantidade
    FROM vendas_ecommerce
    GROUP BY Category;
""")
for row in cursor.fetchall():
    print(row)

# 7. Total de vendas por região
cursor.execute("""
    SELECT Region, SUM(TotalValue) AS TotalPorRegiao
    FROM vendas_ecommerce
    GROUP BY Region;
""")
for row in cursor.fetchall():
    print(row)

# Encerrar conexão
cursor.close()
conn.close()


