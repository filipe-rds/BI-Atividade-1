import pandas as pd
from sqlalchemy import create_engine
import os

# Create a SQLAlchemy engine
engine = create_engine('postgresql+psycopg://user:password@localhost:5432/mydatabase')

# Caminho para o diretório que contém os arquivos CSV
caminho_diretorio = '../'  # Sobe um nível para acessar 'data/normalized'

# Lista dos arquivos CSV na ordem desejada
arquivos_desejados = [
    'transportadoras.csv',
    'categorias.csv',
    'vendedores.csv',
    'fornecedores.csv',
    'paises.csv',
    'clientes.csv',
    'pedidos.csv',
    'produtos.csv',
    'vendas.csv',
]

# Função para converter colunas específicas
def converter_colunas(df, tabela):
    if tabela == 'pedidos':
        # Converter a coluna 'data' para o tipo datetime
        df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')
    # Adicione mais conversões conforme necessário para outras tabelas
    return df

# Listar e processar os arquivos CSV na ordem especificada
for arquivo in arquivos_desejados:
    caminho_arquivo = os.path.join(caminho_diretorio, arquivo)
    
    if os.path.exists(caminho_arquivo):  # Verifica se o arquivo existe
        # Ler o arquivo CSV usando pandas
        df = pd.read_csv(caminho_arquivo)

        # Converter colunas conforme necessário
        tabela = os.path.splitext(arquivo)[0]
        df = converter_colunas(df, tabela)

        # Inserir os dados no banco de dados
        try:
            df.to_sql(tabela, engine, if_exists='append', index=False)
            print(f"Dados inseridos na tabela {tabela} com sucesso.")
        except Exception as e:
            print(f"Erro ao inserir dados na tabela {tabela}: {e}")
    else:
        print(f"Arquivo {arquivo} não encontrado no diretório.")

# Fechar a conexão
engine.dispose()
