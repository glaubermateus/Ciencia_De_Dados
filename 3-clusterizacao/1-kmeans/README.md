# Título do projeto: Clusterização de Clientes

## 💡 Resumo do projeto

Este projeto tem como objetivo aplicar técnicas de aprendizado de máquina não supervisionado para identificar grupos de clientes com comportamentos semelhantes. A análise foi conduzida com o algoritmo K-Means, permitindo segmentar a base de clientes e compreender os diferentes perfis de consumo.

Os resultados apontaram três clusters principais, que representam perfis distintos em termos de idade, gasto mensal, tempo de assinatura e propensão ao cancelamento — fornecendo subsídios para ações de marketing, retenção e fidelização.

## ❓ Problema de negócio / Contexto

Empresas que oferecem serviços por assinatura enfrentam o desafio de entender a diversidade de seus clientes: alguns usam intensamente o serviço, outros gastam pouco ou cancelam rapidamente.
A clusterização foi utilizada para identificar padrões de comportamento e responder a perguntas como:

* Quais são os principais perfis de clientes?
* Que grupos apresentam maior risco de cancelamento?
* Há oportunidades para aumentar o engajamento ou o ticket médio em certos segmentos?

A partir desses agrupamentos, a empresa pode personalizar ofertas, melhorar o atendimento e direcionar estratégias de retenção de forma mais eficaz.

## 📊 Dados utilizados

O dataset contém informações de clientes e suas características de uso do serviço, incluindo:

* Idade
* Gasto_Mensal
* Tempo_de_Assinatura
* Taxa_de_Uso
* Suporte_Tickets
* Cancelou (variável binária, onde 0 = ativo e 1 = cancelado)

Durante o tratamento inicial, foram verificadas duplicidades, valores ausentes e tipos de dados. As variáveis foram padronizadas com o StandardScaler antes da clusterização.

## 🛠️ Metodologia e ferramentas

A metodologia do projeto seguiu as seguintes etapas:

1. Análise exploratória dos dados (EDA) – inspeção de estrutura, valores nulos, estatísticas descritivas e amostras.
2. Padronização das variáveis – uso de StandardScaler para garantir comparabilidade entre atributos em diferentes escalas.
3. Aplicação do algoritmo K-Means – definição do número ótimo de clusters com base na métrica do cotovelo (Elbow Method) e Silhouette Score.
4. Interpretação dos clusters – análise do perfil médio de cada grupo e dos indicadores de engajamento e cancelamento.
5. Geração de insights de negócio – identificação de oportunidades de retenção e aumento de receita.

## Principais bibliotecas utilizadas:

```pandas```, ```numpy```, ```matplotlib```, ```seaborn```, ```scikit-learn```, ```scipy```

## 📈 Principais insights e resultados

A análise resultou em três clusters bem definidos, com perfis distintos:

| Cluster | Perfil                             | Idade Média | Gasto Mensal | Tempo de Assinatura | Taxa de Cancelamento | Insight                          | Ação                                    |
|---------|------------------------------------|-------------|--------------|---------------------|----------------------|----------------------------------|-----------------------------------------|
| 1       | jovens, novos, baixo uso           | ~25 anos    | R$ 302       | 5,6 meses           | 3%                   | alta retenção, baixo engajamento | foco em upsell                          |
| 2       | antigos, alto gasto, insatisfeitos | ~55 anos    | 924          | 20 meses            | 89%                  | alto valor, alto churn           | foco em retenção e suporte              |
| 3       | intermediários e voláteis          | ~38 aos     | 698          | 15 meses            | 54%                  | grupo instável                   | fidelizar e aumentar percepção de valor |


## 🔎 Principais conclusões:

* O Cluster 1 representa clientes novos e estáveis — ótimo público para campanhas de crescimento.
* O Cluster 2 é crítico — alto valor, mas alta taxa de cancelamento, exigindo ações imediatas de retenção.
* O Cluster 3 mostra comportamento intermediário, demandando programas de fidelidade e reengajamento.

Esses resultados fornecem insumos estratégicos para segmentação de campanhas, alocação de recursos de marketing e priorização de atendimento.

## 🚀 Como executar o projeto

*Pré-requisitos:*

Python 3.8+

Jupyter Notebook

Pacotes: ```pandas```, ```numpy```, ```scipy```, ```scikit-learn```, ```matplotlib```, ```seaborn```

*Passos de execução:*

1. Clone o repositório do projeto:

git clone https://github.com/glaubermateus/Ciencia_De_Dados/3-clusterizacao/1-kmeans.git

2. Instale as dependências:

pip install -r requirements.txt

3. Abra o notebook no Jupyter:

jupyter notebook Clusterizacao.ipynb

4. Execute as células em ordem para reproduzir os resultados e gráficos de segmentação.

## 🔗 Contato

Glauber Cruz

Linkedin
https://www.linkedin.com/in/glauber-cruz-6213281b0/

Portfólio
https://sites.google.com/view/glaubercruz/p%C3%A1gina-inicial
