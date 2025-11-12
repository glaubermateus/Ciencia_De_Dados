# Modelagem Estatística: Regressão Linear Múltipla para entender relação entre variáveis

## 💡 Resumo do projeto

Este projeto tem como objetivo analisar como diferentes variáveis socioeconômicas e estruturais influenciam a taxa de ocupação de um bairro, por meio de um modelo de Regressão Linear Múltipla. A análise busca identificar os principais fatores que explicam o comportamento da taxa de ocupação e mensurar o impacto de cada variável preditora.

## ❓ Problema de negócio / contexto

Compreender o que determina a taxa de ocupação é essencial para o planejamento urbano e imobiliário. A administração pública e investidores privados precisam identificar quais variáveis mais contribuem para a ocupação ou desocupação de áreas residenciais, a fim de direcionar políticas públicas, investimentos e estratégias de desenvolvimento urbano.

O projeto parte da seguinte pergunta:

* Quais fatores explicam as variações na taxa de ocupação dos bairros? Como cada variável influencia esse indicador?

## 📊 Dados utilizados

* Fonte: Base de dados local com indicadores urbanos e socioeconômicos.
* Tamanho: 14 variáveis preditoras + 1 variável resposta (taxa de ocupação).
* Principais variáveis:
    * numero_medio_quartos_por_residencia
    * idade_media_residencias
    * taxa_criminalidade
    * proporcao_empresas
    * distancia_centro
    * taxa_poluicao
    * imposto_residencial

* Tratamentos realizados:
    * Renomeação de colunas para melhor legibilidade
    * Checagem de valores ausentes e duplicados
    * Análise estatística descritiva
    * Visualização dos dados

## 🛠️ Metodologia e ferramentas

1. Análise Exploratória de Dados (EDA):
* Estatísticas descritivas e distribuição das variáveis
* Identificação de outliers e correlação entre variáveis
* Visualizações com matplotlib e seaborn

2. Modelagem Estatística:
* Aplicação do modelo de Regressão Linear Múltipla usando o pacote statsmodels
* Avaliação dos coeficientes e significância estatística (p-valores)
* Testes de aderência e diagnóstico dos resíduos (normalidade, homocedasticidade, independência)
* Métricas de desempenho: R², R² ajustado e análise do erro padrão dos coeficientes

3. Ferramentas e bibliotecas utilizadas:
* Linguagem Python
* ```pandas``` e ```numpy```: manipulação e preparação dos dados
* ```matplotlib``` e ```seaborn```: visualização dos dados
* ```scipy``` e ```statsmodels```: análise estatística e modelagem

## 📈 Principais insights e resultados

O modelo apresentou bom ajuste (R² = 0.72), indicando que as variáveis escolhidas explicam grande parte da variação da taxa de ocupação.

As variáveis selecionadas para o modelo foram:

* numero_medio_quartos_por_residencia
* taxa_criminalidade
* distancia_centro
* taxa_professores
* taxa_desabrigados

A variável 'numero_medio_quartos_por_residencia' foi a única que teve impacto positivo na variável-alvo 'taxa_ocupacao'. As demais tiveram influência negativa na variável resposta.

## 📊 Conclusão:
O modelo permite compreender de forma quantitativa como aspectos urbanos e econômicos influenciam a densidade e atratividade residencial dos bairros, podendo ser usado como base para planejamento urbano e decisões de investimento.

É importante enfatizar que, para utilizar o modelo de regressão linear, faz-se necessário validar as suposições do modelo, fica como sugestão para um trabalho complementar. As suposições são as seguintes:

* linearidade entre as variáveis
* independência dos resíduos
* homoscedasticidade (variância dos resíduos constante)
* normalização dos resíduos
* sem multicolinearidade



## 🚀 Como executar o projeto

**Pré-requisitos:**

* Python 3.10+
* Jupyter Notebook
* Bibliotecas: ```pandas```, ```numpy```, ```matplotlib```, ```seaborn```, ```scipy```, ```statsmodels```

## 🤝 Contato

Glauber Cruz

[Linkedin](https://www.linkedin.com/in/glauber-cruz-6213281b0/)

[Portfolio](https://sites.google.com/view/glaubercruz/p%C3%A1gina-inicial)
