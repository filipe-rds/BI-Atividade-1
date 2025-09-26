<div align="center">

# Análise de Vendas Globais - Business Intelligence

![Python](https://img.shields.io/badge/Python-3.12+-blue?style=flat-square&logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Latest-blue?style=flat-square&logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Latest-blue?style=flat-square&logo=docker)
![Jupyter](https://img.shields.io/badge/Jupyter-Lab-orange?style=flat-square&logo=jupyter)
![Status](https://img.shields.io/badge/Status-Concluído-green?style=flat-square)

</div>

## Sobre o Projeto

Este projeto apresenta uma análise completa de vendas globais desenvolvida em resposta às demandas estratégicas do Departamento de Vendas. O objetivo é processar, analisar e visualizar dados de vendas para fornecer insights acionáveis que apoiem a tomada de decisão empresarial.

### Objetivos

- Processar e normalizar dados de vendas globais
- Criar ambiente de análise robusto e escalável
- Responder 10 perguntas estratégicas de negócio
- Fornecer insights visuais através de gráficos e métricas

## Principais Análises Realizadas

> 📊 **[Abrir Notebook Interativo](./notebooks/notebook.ipynb)** - Acesse todas as análises com gráficos e código executável

### 1. Top 10 Maiores Clientes

Identificação dos principais clientes por volume de vendas ($), com análise de concentração e participação de mercado.

### 2. Ranking dos 3 Maiores Países

Análise geográfica das vendas, identificando os mercados mais lucrativos globalmente.

### 3. Categorias de Produtos - Brasil

Mapeamento das categorias de produtos com maior faturamento especificamente no mercado brasileiro.

### 4. Análise de Frete por Transportadora

Avaliação completa das despesas de frete e distribuição de custos entre transportadoras parceiras.

### 5. Segmento Calçados Masculinos - Alemanha

Análise segmentada do mercado alemão para produtos de calçados masculinos.

### 6. Vendedores com Maiores Descontos - EUA

Identificação de padrões de desconto no mercado americano por vendedor.

### 7. Fornecedores de Vestuário Feminino

Análise de margem de lucro no segmento de vestuário feminino por fornecedor.

### 8. Evolução Temporal (2009-2012)

Análise do histórico de vendas anuais no período de 2009 a 2012.

### 9. Calçados Masculinos em 2012

Análise detalhada por clientes e distribuição geográfica (cidades) em 2012.

### 10. Vendas na Europa por País

Mapeamento completo do desempenho de vendas em países europeus.

> 📚 **[Abrir Conclusões Finais](./assets/final-conclusions.pdf)** - Acesse todas as análises respondidas de forma direta em PDF

## Arquitetura da Solução

### Backend de Dados

- **PostgreSQL**: Banco de dados relacional para armazenamento estruturado
- **Docker**: Containerização para ambiente consistente e reproduzível

### Análise e Visualização

- **Jupyter Lab**: Ambiente interativo para análise exploratória
- **Python 3.12+**: Linguagem principal para processamento
- **Pandas**: Manipulação e análise de datasets
- **Matplotlib & Seaborn**: Visualizações estáticas
- **Plotly**: Gráficos interativos e dashboards
- **SQLAlchemy**: ORM para integração Python-PostgreSQL

## Estrutura do Projeto

```
BI-Atividade-1/
├── notebooks/
│   └── notebook.ipynb           # Análises completas com visualizações
├── data/
│   ├── original/               # Dados brutos CSV
│   └── normalized/             # Dados processados e normalizados
├── db/
│   └── db.sql                  # Schema e dados do PostgreSQL
├── docker-compose.yml          # Orquestração de containers
├── requirements.txt            # Dependências Python
└── README.md                   # Este arquivo
```

## Como Executar o Projeto

### Pré-requisitos

- Docker & Docker Compose
- Navegador web moderno

### Execução

1. **Clone e acesse o diretório**

```bash
git clone <url-do-repositorio>
cd "BI-Atividade-1"
```

2. **Inicie os serviços**

```bash
docker-compose up -d
```

3. **Acesse o Jupyter Lab**

- **URL**: http://localhost:8888
- **Token**: Removido para facilitar desenvolvimento

4. **Configuração do Banco**

| Parâmetro | Valor          |
| --------- | -------------- |
| Host      | localhost:5432 |
| User      | user           |
| Password  | password       |
| Database  | mydatabase     |

## Modelo Lógico de Dados

### Estrutura das Tabelas

**PAISES**

- id (CHAR(3)) - PK
- nome (VARCHAR(255))

**CATEGORIAS**

- id (SERIAL) - PK
- nome (VARCHAR(255))
- descricao (TEXT)

**FORNECEDORES**

- id (SERIAL) - PK
- nome (VARCHAR(255))

**VENDEDORES**

- id (SERIAL) - PK
- nome (VARCHAR(255))

**TRANSPORTADORAS**

- id (SERIAL) - PK
- nome (VARCHAR(255))

**CLIENTES**

- id (SERIAL) - PK
- pais_id (CHAR(3)) - FK → PAISES.id
- nome (VARCHAR(255))
- contato (VARCHAR(255))
- cidade (VARCHAR(255))

**PEDIDOS**

- id (SERIAL) - PK
- cliente_id (INT) - FK → CLIENTES.id
- vendedor_id (INT) - FK → VENDEDORES.id
- data (DATE)

**PRODUTOS**

- id (SERIAL) - PK
- fornecedor_id (INT) - FK → FORNECEDORES.id
- categoria_id (INT) - FK → CATEGORIAS.id
- nome (VARCHAR(255))

**VENDAS**

- id (SERIAL) - PK
- pedido_id (INT) - FK → PEDIDOS.id
- produto_id (INT) - FK → PRODUTOS.id
- transportadora_id (INT) - FK → TRANSPORTADORAS.id
- quantidade (INT)
- valor_vendas (DECIMAL(10,2))
- custo_vendas (DECIMAL(10,2))
- margem_bruta (DECIMAL(10,2))
- frete (DECIMAL(10,2))
- desconto (DECIMAL(10,2))

### Relacionamentos

- PAISES (1) → CLIENTES (N)
- CLIENTES (1) → PEDIDOS (N)
- VENDEDORES (1) → PEDIDOS (N)
- PEDIDOS (1) → VENDAS (N)
- PRODUTOS (1) → VENDAS (N)
- FORNECEDORES (1) → PRODUTOS (N)
- CATEGORIAS (1) → PRODUTOS (N)
- TRANSPORTADORAS (1) → VENDAS (N)

### Tabelas Principais

| Tabela              | Descrição             | Registros |
| ------------------- | --------------------- | --------- |
| **clientes**        | Dados de clientes     | 91        |
| **paises**          | Países                | 23        |
| **produtos**        | Catálogo              | 77        |
| **categorias**      | Segmentos             | 8         |
| **transportadoras** | Logística             | 3         |
| **vendedores**      | Equipe de vendas      | 9         |
| **fornecedores**    | Parceiros             | 29        |
| **vendas**          | Transações detalhadas | 2.173     |

## Principais Insights

### Performance de Vendas

- **Crescimento**: Faturamento cresceu consistentemente entre 2009-2012
- **Concentração**: Top 10 clientes representam parcela significativa das vendas
- **Geografia**: EUA, Alemanha e França lideram vendas globais

### Segmentação

- **Brasil**: Forte desempenho em categorias específicas
- **Europa**: Distribuição equilibrada entre países
- **EUA**: Padrões de desconto bem definidos

### Operacional

- **Frete**: Custos concentrados em transportadoras específicas
- **Margens**: Vestuário feminino apresenta margens atrativas
- **Sazonalidade**: Padrões identificados por período

## Stack Tecnológica

| Tecnologia      | Versão | Propósito                 |
| --------------- | ------ | ------------------------- |
| **Python**      | 3.12+  | Processamento e análise   |
| **PostgreSQL**  | Latest | Banco de dados relacional |
| **Jupyter Lab** | Latest | Ambiente de análise       |
| **Docker**      | Latest | Containerização           |
| **Pandas**      | 2.3+   | Manipulação de dados      |
| **Matplotlib**  | Latest | Visualizações estáticas   |
| **Seaborn**     | Latest | Gráficos estatísticos     |
| **Plotly**      | Latest | Visualizações interativas |
| **SQLAlchemy**  | Latest | ORM Python-SQL            |

## Métricas do Projeto

| Métrica           | Valor  | Descrição                          |
| ----------------- | ------ | ---------------------------------- |
| **Datasets**      | 9      | Tabelas normalizadas               |
| **Análises**      | 10     | Questões estratégicas              |
| **Visualizações** | 17     | Gráficos (estáticos + interativos) |
| **Registros**     | 2.173  | Transações de vendas               |
| **Países**        | 23     | Mercados globais                   |
| **Período**       | 4 anos | 2009-2012                          |
| **Células**       | 21     | Células analíticas                 |
| **Linhas**        | 3.682  | Linhas no notebook                 |

## Equipe de Desenvolvimento

| Nome                 | Função               |
| -------------------- | -------------------- |
| **Danillo Coelho**   | Analista de Sistemas |
| **Filipe Rodrigues** | Analista de Sistemas |
| **Gabriel Macaúbas** | Analista de Sistemas |
| **Lucas Andrade**    | Analista de Sistemas |

---

<div align="center">

**Desenvolvido pela equipe de Business Intelligence**

_Transformando dados em insights acionáveis_

</div>
