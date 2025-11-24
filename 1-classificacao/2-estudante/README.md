# Classificação – Avaliando o Uso da IA

## 💡 Resumo do projeto

Este projeto aplica técnicas de Machine Learning para prever se um usuário obteve sucesso ao utilizar uma ferramenta de IA, com base em variáveis coletadas sobre seu comportamento, experiência e percepção durante o uso.

## ❓ Problema de negócio / contexto

Com a crescente adoção de ferramentas de IA, muitas empresas querem entender quando a IA realmente entrega valor para os usuários — e quando ela falha (ex.: ideias ruins, alucinações, respostas não úteis).
Este projeto tem como objetivo responder à seguinte questão:

**É possível prever se o usuário terá um uso bem-sucedido da IA?**

A resposta para essa pergunta pode ajudar a melhorar produtos de IA, otimizar experiências e orientar decisões de design.

## 📊 Dados utilizados

O dataset apresenta respostas de usuários após experiências com IA.

Algumas das variáveis do dataset são:

* expectativa de uso
* avaliação do resultado
* intenção de uso futuro
* percepções subjetivas sobre qualidade das respostas
* métricas de facilidade, utilidade e sucesso

Tratamentos realizados: 

* Limpeza e padronização dos dados
* Conversão de variáveis categóricas
* Avaliação de valores extremos (outliers)
* Confirmamos hipóteses iniciais com inspeção visual

## 🛠️ Metodologia e ferramentas

**Principais etapas**

1. Carregamento dos dados e importação das bibliotecas
2. Limpeza e transformação dos atributos
3. Análise exploratória (EDA)
4. Visualização de padrões e relações entre variáveis

**Pré-processamento para Machine Learning**

* Normalização
* Encoding
* Divisão dos dados em treino e teste
* Treinamento de modelos de classificação
* Avaliação do desempenho dos modelos

**Ferramentas utilizadas**

* Python
* Bibliotecas: ```pandas```, ```numpy```, ```matplotlib```, ```seaborn``` e ```scikit-learn```

## 📈 Principais insights e resultados

* As análises gráficas confirmaram que muitos usuários tiveram suas expectativas atendidas pela IA.

* Quando o uso não foi bem-sucedido, os motivos mais comuns foram:

    * alucinações da IA,
    * respostas confusas,
    * dificuldade de entender instruções.

Observou-se também um grupo curioso: usuários que atingiram o objetivo, mas não usariam IA novamente, possivelmente por desconforto ou baixa confiança.

**Valor gerado**

O modelo auxilia equipes de produto a identificar perfis de usuários mais propensos a sucesso.

A análise estatística e visual revela pontos críticos a serem ajustados na experiência da IA.

## 🚀 Como executar o projeto

**Pré-requisitos:**

* Python 3.9+

* Jupyter Notebook ou VS Code

* Clonar o repositório

git clone https://github.com/glaubermateus/Ciencia_De_Dados/1-classificacao/2-estudante.git

* Instalar dependências

```pip install -r requirements.txt```

* Executar o notebook

```jupyter notebook ML_Classificacao_Usou_IA.ipynb```

## 🤝 Contato

Glauber Cruz

[LinkedIn](https://www.linkedin.com/in/glauber-cruz-6213281b0/)

[Portfólio](https://sites.google.com/view/glaubercruz/p%C3%A1gina-inicial)
