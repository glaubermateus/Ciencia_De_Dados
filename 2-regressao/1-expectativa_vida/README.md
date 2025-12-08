# Modelagem Preditiva: análise de regressão para prever expectativa de vida

## 💡 Resumo do projeto

Esse projeto consiste em criar um modelo de regressão linear para estimar a expectativa de vida de países com base em indicadores socioeconômicos, demográficos e de saúde utilizando técnicas de Machine Learning.

## ❓ Problema de negócio / contexto

Organizações públicas e privadas precisam entender quais fatores mais impactam a expectativa de vida de uma população. Esse tipo de informação é essencial para:

* Planejamento de políticas públicas
* Investimentos em saúde
* Análise de desenvolvimento humano

O objetivo do projeto foi responder às seguintes questões:

1. É possível prever a expectativa de vida de um país apenas com variáveis socioeconômicas e de saúde?
2. Quais fatores têm maior influência nesse indicador?

## 📊 Dados utilizados

Dataset público contendo informações por país e ano, com foco em saúde e desenvolvimento humano.

**Principais variáveis utilizadas:**

* Expectativa de vida (variável alvo)
* Taxas de mortalidade
* Nível de escolaridade
* Renda per capita
* Gastos com saúde
* Dados relacionados a imunização

**Tratamentos aplicados:**

* Análise e tratamento de valores ausentes
* Análise e tratamento de outliers
* Padronização de variáveis numéricas
* Validação de tipos de dados
* Análise de multicolinearidade
* Seleção de features

## 🛠️ Metodologia e ferramentas

**Etapas do projeto**

1. Importação das bibliotecas e carregamento dos dados
2. Limpeza e preparação dos dados
3. Análise Exploratória (EDA)
    * Estatísticas descritivas
    * Matriz de correlação
    * Visualizações gráficas
4. Pré-processamento
    * Normalização / padronização
    * Separação em treino e teste
5. Treinamento de modelos de regressão
    * Regressão Linear
    * Outros modelos para comparação (Ridge, Lasso e Ridge com otimização de hiperparâmetros)
6. Avaliação de desempenho dos modelos
    * R²
    * MAE
    * RMSE

**Ferramentas utilizadas**
* Linguagem Python

**Bibliotecas:**
* ```pandas```
* ```numpy```
* ```matplotlib```
* ```seaborn```
* ```scikit-learn```

## 📈 Principais insights e resultados

* Indicadores ligados a saúde e educação foram os fatores com maior impacto na expectativa de vida.
* O modelo de regressão linear sem otimização de hiperparâmetros apresentou bom poder explicativo, alcançando métricas satisfatórias de desempenho.

**Valor gerado**
* Apoio à tomada de decisão em políticas públicas
* Identificação de fatores críticos para aumento da longevidade
* Base para construção de análises preditivas mais avançadas

## 🚀 Como executar o projeto

**Pré-requisitos**

* Python 3.9 ou superior
* Jupyter Notebook

* Clonar o repositório

```git clone https://github.com/glaubermateus/Ciencia_De_Dados/tree/main/2-regressao/1-expectativa_vida.git```

* Instalar dependências:

```pip install -r requirements.txt```

Executar o projeto

```jupyter notebook Projeto_Regressao_Expectativa_Vida.ipynb```

## 🤝 Contato

Glauber Cruz

[LinkedIn](https://www.linkedin.com/in/glauber-cruz-6213281b0/)

[Portfólio](https://sites.google.com/view/glaubercruz/p%C3%A1gina-inicial)
