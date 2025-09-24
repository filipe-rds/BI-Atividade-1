# 📊 Projeto de Análise de Vendas - Business Intelligence

## 📋 Descrição do Projeto

Este projeto foi desenvolvido pela equipe de **Analistas de Sistemas** em resposta a uma demanda do **Departamento de Vendas**. O objetivo é processar e analisar um conjunto de dados de vendas fornecidos em formato CSV para responder a perguntas específicas de negócio.

## 🎯 Objetivos

- Processar e normalizar dados de vendas globais
- Criar um ambiente de análise robusto e escalável
- Responder perguntas estratégicas do Departamento de Vendas
- Fornecer insights acionáveis para tomada de decisão

## 🏗️ Arquitetura da Solução

Nossa solução utiliza uma stack moderna de tecnologias:

### **Backend de Dados**

- **PostgreSQL**: Banco de dados relacional para armazenamento estruturado
- **Docker**: Containerização para ambiente consistente e portável

### **Análise e Visualização**

- **Jupyter Lab**: Ambiente interativo para análise de dados
- **Python**: Linguagem principal para processamento
  - **Pandas**: Manipulação e análise de dados
  - **SQLAlchemy**: ORM para integração com banco de dados

## 📁 Estrutura do Projeto

```
├── dados brutos/           # Arquivos CSV originais do Departamento de Vendas
├── dados normalizados/     # Dados processados e normalizados
├── data/
│   ├── original/          # Scripts de processamento de dados
│   └── normalized/        # Dados finais normalizados
├── db/
│   └── tables.sql         # Schema do banco de dados
├── myenv/                 # Ambiente virtual Python
├── docker-compose.yml     # Configuração dos serviços
└── README.md             # Este arquivo
```

## 🚀 Como Executar o Projeto

### **Pré-requisitos**

- Docker e Docker Compose instalados
- Git (para clonar o repositório)

### **Passo a Passo**

1. **Clone o repositório**

   ```bash
   git clone <url-do-repositorio>
   cd "BI-atividade-1"
   ```

2. **Inicie os serviços**

   ```bash
   docker-compose up -d
   ```

3. **Acesse o Jupyter Lab**

   - Abra o navegador em: `http://localhost:8888`
   - O token de acesso foi removido para facilitar o desenvolvimento

4. **Conecte ao banco de dados**
   - **Host**: localhost
   - **Porta**: 5432
   - **Usuário**: user
   - **Senha**: password
   - **Database**: mydatabase

## 📊 Modelo de Dados

O projeto implementa um modelo de dados normalizado com as seguintes tabelas:

- **📋 pedidos**: Informações dos pedidos (cliente, vendedor, data)
- **👥 clientes**: Dados dos clientes (nome, contato, localização)
- **🌍 paises**: Países dos clientes
- **📦 produtos**: Catálogo de produtos
- **🏷️ categorias**: Categorias dos produtos
- **🚚 transportadoras**: Empresas de transporte
- **👨‍💼 vendedores**: Equipe de vendas
- **💰 vendas**: Transações detalhadas (quantidade, valores, margem)

## 🛠️ Tecnologias Utilizadas

| Tecnologia  | Versão | Uso                    |
| ----------- | ------ | ---------------------- |
| Python      | 3.12+  | Processamento de dados |
| PostgreSQL  | Latest | Banco de dados         |
| Jupyter Lab | Latest | Análise interativa     |
| Docker      | Latest | Containerização        |
| Pandas      | 2.3+   | Manipulação de dados   |
| SQLAlchemy  | Latest | ORM Python-SQL         |
