# Testes de Hipóteses em Python


## 💡 Resumo do projeto

Este projeto tem como objetivo demonstrar a aplicação prática de testes de hipóteses estatísticas em Python, comparando diferentes abordagens — paramétricas e não paramétricas — para a análise de grupos e variáveis. A análise visa mostrar como esses testes auxiliam na validação de inferências sobre populações a partir de amostras.


## ❓ Problema de negócio / Contexto

No contexto de análise de dados, é comum a necessidade de verificar se diferenças observadas entre grupos são estatisticamente significativas ou se ocorreram apenas por acaso. No contexto em questão, o objetivo foi verificar se, numa base de dados de saúde, a variável categórica 'genero' (Masculino/Feminino) se relaciona de alguma forma com a variável categórica 'alcool' (0 - não consome álcool / 1 - consome álcool). A partir disso, este projeto busca responder perguntas como:

* Existe diferença estatística entre a taxa de álcool dos grupos masculino e feminino?
* Há associação entre as variáveis gênero e álcool? Em outra palavras, ser homem ou mulher influencia no consumo de álcool?

Para isso, são aplicados testes como o t de Student, Qui-quadrado e Mann-Whitney, de modo a ilustrar a importância da validação estatística em tomadas de decisão baseadas em dados.


## 📊 Dados utilizados

Os dados utilizados neste projeto foram importados e tratados diretamente em Python, sendo compostos por variáveis contínuas e categóricas.
Durante o processo, foram realizadas:

* Análises de distribuição e verificação de normalidade;
* Criação de tabelas de contingência;
* Verificação de suposições estatísticas (normalidade, homocedasticidade e presença de outliers)


## 🛠️ Metodologia e ferramentas

A metodologia foi estruturada em três etapas principais:

1. Exploração dos conceitos estatísticos: revisão teórica sobre testes paramétricos e não paramétricos.

2. Aplicação prática em Python: uso de testes t, Qui-quadrado e Mann-Whitney no dataset de exemplo.

3. Interpretação dos resultados: análise dos valores de p-valor, intervalos de confiança e significância estatística.


## Ferramentas e bibliotecas utilizadas:

🐍 Python 3.12

🐼 pandas → manipulação e análise de dados

📈 scipy.stats → execução dos testes estatísticos

🧮 numpy → cálculos numéricos

📊 matplotlib / seaborn → visualização gráfica


🔎 Principais insights e resultados

* Testes paramétricos (como o t de Student) devem ser preferencialmente utilizados quando as suposições são atendidas (normalidade e homogeneidade de variâncias), pois fornecem maior robustez e precisão nas inferências.

* Testes não paramétricos (como o Qui-quadrado e Mann-Whitney) são alternativas importantes quando as suposições dos testes paramétricos não são válidas.

* A validação estatística evita conclusões baseadas apenas em observações descritivas, garantindo que diferenças entre grupos sejam de fato significativas e não fruto do acaso.


Em resumo, os testes estatísticos são fundamentais para a tomada de decisão orientada por dados, conferindo confiabilidade e rigor científico às análises realizadas.

## 🚀 Como executar o projeto

### Pré-requisitos:

* Python 3.8 ou superior
* Jupyter Notebook
* Pacotes: ```pandas```, ```numpy```, ```scipy```, ```matplotlib```, ```seaborn```

Execução:

1. Clone o repositório do projeto:

git clone https://github.com/usuario/teste-hipotese-python.git

2. Instale as dependências:

pip install -r requirements.txt

3. Abra o Jupyter Notebook e execute o arquivo:

jupyter notebook Projeto_Teste_Hipotese.ipynb

4. Siga as instruções no notebook para reproduzir as análises e interpretar os resultados.

## 🧷 Contato

Glauber Cruz

LinkedIn:
https://www.linkedin.com/in/glauber-cruz-6213281b0/

Portfólio:
https://sites.google.com/view/glaubercruz/p%C3%A1gina-inicial
