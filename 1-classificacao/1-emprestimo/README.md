# 🏦 Modelo de Classificação para Aprovação de Empréstimos

## 💡 Resumo do projeto

Esse projeto foi criado com foco em desenvolver um modelo preditivo capaz de prever se um cliente terá seu empréstimo aprovado com base em atributos socioeconômicos e financeiros. O projeto inclui análise exploratória, preparação dos dados e avaliação de diferentes algoritmos de classificação.

## ❓ Problema de negócio / contexto

Instituições financeiras precisam avaliar rapidamente o risco de conceder crédito. Esse processo costuma envolver análise manual, burocrática e sujeita a inconsistências. O objetivo deste projeto é automatizar essa etapa usando um modelo preditivo de classificação, capaz de estimar se um empréstimo deve ser aprovado ou não com base no perfil do solicitante.

## 📊 Dados utilizados

Os dados do projeto provém de um dataset de empréstimos contendo variáveis de perfil, renda, histórico de crédito e características do financiamento.

- Atributos principais:

    - Gênero
    - Estado civil
    - Número de dependentes
    - Nível educacional
    - Autônomo
    - Renda requerente
    - Renda corequerente
    - Valor do empréstimo
    - Tempo de empréstimo
    - Histórico de crédito
    - Propriedade
    - Status do empréstimo (variável alvo)

- O dataset foi carregado a partir do notebook.

- Foram aplicados tratamentos como:

    - Verificação e imputação de valores ausentes

    - Ajustes de tipos de dados

    - Padronização e transformação de variáveis numéricas

    - Codificação de variáveis categóricas

## 🛠️ Metodologia e ferramentas

Ferramentas utilizadas:

- Python

- Bibliotecas: ```pandas```, ```numpy```, ```matplotlib```, ```seaborn```, ```scikit-learn```

**Etapas da análise**

1. Análise exploratória (EDA):

    - inspeção da estrutura dos dados, análise de distribuição e correlações.

2. Pré-processamento:

    - Tratamento de missing values

    - Normalização de atributos numéricos

    - Codificação de categorias

    - Split entre treino e teste

3. Modelagem preditiva:

    - Treinamento de classificadores (Ex.: Logistic Regression, Random Forest, etc.)

    - Avaliação de performance com métricas como Acurácia, AUC, Precision e Recall

    - Interpretação dos resultados: análise de variáveis relevantes e impacto no modelo.

## 📈 Principais insights e resultados

O histórico de crédito (Credit_History) foi a variável mais determinante para a aprovação de empréstimo.

A renda do solicitante e o valor do empréstimo também apresentaram impacto significativo.

Os modelos avaliados apresentaram boa performance e foi possível atingir métricas consistentes para apoiar decisões de concessão de crédito.

A análise sugere que o modelo pode automatizar parte do processo, reduzindo tempo e aumentando consistência na avaliação dos casos.

O modelo que apresentou melhor performance em treino e teste foi o algoritmo Ada Boost com 0.86 aproximadamente nas métricas de validação.

Não conseguimos aumentar a precisão do modelo com otimização de hiperparâmetros, indicando que, para esse conjunto de dados, os hiperparâmetros default do Ada Boost alcançaram melhor performance do modelo.

## 🚀 Como executar o projeto

**Pré-requisitos:**

* Python 3.9+

* pip ou conda

**Passos**

1. Clonar o repositório:

```git clone https://github.com/glaubermateus/Ciencia_De_Dados.git```

2. Instalar dependências

```pip install -r requirements.txt```

3. Executar o notebook

Abra no Jupyter Notebook ou no VS Code:

```jupyter notebook Projeto_Classificacao_Emprestimo.ipynb```

## 🤝 Contato

Glauber Cruz

[LinkedIn](https://www.linkedin.com/in/glauber-cruz-6213281b0/)

[Portfólio](https://sites.google.com/view/glaubercruz/p%C3%A1gina-inicial)
