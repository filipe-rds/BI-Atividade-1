import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('vendas_globais.csv')

# Tabela 1: Pedidos
pedidos = df[['PedidoID', 'ClienteID', 'VendedorID', 'Data']].drop_duplicates()
pedidos.columns = ['id', 'cliente_id', 'vendedor_id', 'data']

# Tabela 2: Clientes
clientes = df[['ClienteID','ClientePaísID', 'ClienteNome', 'ClienteContato', 'ClienteCidade']].drop_duplicates()
clientes.columns = ['id', 'pais_id', 'nome', 'contato', 'cidade']

# Tabela 3: Países
paises = df[['ClientePaísID', 'ClientePaís']].drop_duplicates()
paises.columns = ['id', 'nome']

# Tabela 4: Produtos
produtos = df[['ProdutoID', 'ProdutoNome', 'FornecedorID', 'CategoriaID']].drop_duplicates()
produtos.columns = ['id', 'nome', 'fornecedor_id', 'categoria_id']

# Tabela 5: Categorias
categorias = df[['CategoriaID', 'CategoriaNome', 'CategoriaDescrição']].drop_duplicates()
categorias.columns = ['id', 'nome', 'descricao']

# Tabela 6: Vendas
vendas = df[['PedidoID', 'ProdutoID', 'TransportadoraID', 'Qtde', 'Vendas', 'Vendas Custo', 'Margem Bruta', 'Frete', 'Desconto']].drop_duplicates()
vendas.columns = ['pedido_id', 'produto_id', 'transportadora_id', 'quantidade', 'valor_vendas', 'custo_vendas', 'margem_bruta', 'frete', 'desconto']

# Adicionar um ID único no início da tabela vendas
vendas.insert(0, 'id', range(1, len(vendas) + 1))

# Salvar os DataFrames em arquivos CSV
pedidos.to_csv('pedidos.csv', index=False)
clientes.to_csv('clientes.csv', index=False)
paises.to_csv('paises.csv', index=False)
produtos.to_csv('produtos.csv', index=False)
categorias.to_csv('categorias.csv', index=False)
vendas.to_csv('vendas.csv', index=False)