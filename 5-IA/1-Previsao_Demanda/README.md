# Projeto de Previsão de Demanda e Otimização de Estoque com IA

## 💡 Resumo do projeto

Pipeline de dados automatizado que integra dados de vendas, estoque e sazonalidade para gerar insights de previsão de demanda e recomendações de reabastecimento, utilizando SQLite, Python e LLM (Llama 3) como apoio analítico para decisões de negócio.

## ❓ Problema de negócio / contexto

Empresas de varejo enfrentam dificuldades para equilibrar estoque disponível e demanda futura, especialmente para produtos sazonais.
Estoques excessivos geram custo parado; estoques insuficientes geram perda de vendas.

Este projeto busca responder perguntas como:

- Quais produtos podem sofrer ruptura de estoque?
- Onde há excesso de estoque frente à demanda prevista?
- Como a sazonalidade impacta o comportamento de vendas?
- Quais ações de reabastecimento são recomendadas com base em dados históricos e previsão?

## 📊 Dados utilizados

Os dados são simulados e armazenados em arquivos CSV, representando um cenário realista de varejo:

- Produtos
- Categorias
- Fornecedores
- Clientes
- Vendas
- Estoque
- Sazonalidade
- Forecast de demanda
- Reabastecimento
- Pedidos

**Tratamentos aplicados:**

- Validação de colunas obrigatórias por tabela
- Ingestão controlada no SQLite
- Relacionamento entre tabelas normalizadas
- Consolidação mensal de vendas e forecast
- Cálculo de métricas de erro diretamente no banco

## 🛠️ Metodologia e ferramentas

**Ferramentas**

- Python
- SQLite
- Pandas
- LangChain
- Ollama (Llama 3)
- Logging estruturado
- Subprocess para orquestração

**Metodologia**

1. Criação e carga de dados
    - Leitura de múltiplos CSVs
    - Validação de schema por tabela
    - Inserção incremental no banco SQLite
2. Avaliação de forecast
    - Consolidação mensal de vendas e previsões
    - Cálculo de métricas por produto e categoria (MAE, MSE e MAPE)

3. Integração analítica
    - Query SQL consolidando vendas, estoque, forecast e sazonalidade
    - Enriquecimento do contexto analítico por produto

4. Geração de insights com LLM
    - Criação de batches de produtos
    - Envio de contexto estruturado ao LLM
    - Geração de recomendações em linguagem natural
    - Exportação dos insights para CSV

5. Orquestração do pipeline
    - Execução sequencial dos scripts
    - Logs centralizados por etapa

## 📈 Principais insights e resultados

O pipeline gera automaticamente insights textuais, como:

- Identificação de produtos com alto risco de ruptura
- Produtos com estoque elevado e baixa demanda prevista
- Impacto da sazonalidade nas vendas
- Recomendações de ajuste de estoque e reabastecimento

**Saída final:**

Arquivo ```analise.csv``` contendo os insights gerados pelo modelo de IA, prontos para consumo por áreas de negócio ou dashboards.

## 🚀 Como executar o projeto

**Pré-requisitos**

- Python 3.10+
- SQLite
- Ollama instalado localmente
- Modelo llama3 disponível no Ollama

**1. Clonar o repositório**

```git clone https://github.com/glaubermateus/Engenharia_Dados.git```

```cd seu-repositorio```

**2. Instalar dependências**

```pip install -r requirements.txt```

**3. Executar o projeto**

```python pipeline.py```

O pipeline executa automaticamente:

1. Criação das tabelas no SQLite
2. Carga dos dados CSV
3. Consulta analítica
4. Geração de insights com IA
5. Salvamento dos resultados

## 🤝 Contato

Glauber Cruz

[LinkedIn](https://www.linkedin.com/in/glauber-cruz-6213281b0/)

[Portfólio](https://sites.google.com/view/glaubercruz/p%C3%A1gina-inicial)