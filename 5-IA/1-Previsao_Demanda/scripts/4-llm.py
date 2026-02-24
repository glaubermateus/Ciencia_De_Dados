# Imports
import csv
from utils import nome_arquivo, conectar_banco
from config import logger, analise
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms.ollama import Ollama

# Variáveis
batch_size = 2

# Instanciando o LLM
llm = Ollama(model="llama3")

# Parser de saída
output_parser = StrOutputParser()

# Função utilitária para criar batches
def criar_batches(lista, tamanho):
    for i in range(0, len(lista), tamanho):
        yield lista[i:i + tamanho]

# Função para gerar insights
def buscar_dados():
    try:
        # Conexão com o SQLite
        conn = conectar_banco()
        cursor = conn.cursor()
        
        # Query SQL
        query = """
            SELECT
                p.id_produto,
                p.nome_produto,
                c.nome_categoria,
                f.nome_fornecedor,
                COALESCE(SUM(v.quantidade_vendida), 0) AS total_vendido,
                COALESCE(e.quantidade_em_estoque, 0) AS quantidade_em_estoque,
                COALESCE(s.nome_temporada, 'Nenhuma') AS temporada,
                COALESCE(fore.quantidade_forecast, 0) AS quantidade_forecast,
                COALESCE(re.quantidade, 0) AS quantidade_reabastecida,
                af.mae,
                af.mape
            FROM produtos p
            LEFT JOIN categorias c ON p.id_categoria = c.id_categoria
            LEFT JOIN fornecedores f ON p.id_fornecedor = f.id_fornecedor
            LEFT JOIN vendas v ON p.id_produto = v.id_produto
            LEFT JOIN estoque e ON p.id_produto = e.id_produto
            LEFT JOIN sazonalidade s ON p.id_produto = s.id_produto
            LEFT JOIN forecast fore ON p.id_produto = fore.id_produto
            LEFT JOIN reabastecimento re ON p.id_produto = re.id_produto
            LEFT JOIN (
    SELECT
        id_produto,
        ROUND(AVG(erro_absoluto), 2) AS mae,
        ROUND(AVG(erro_percentual) * 100, 2) AS mape
    FROM avaliacao_forecast
    GROUP BY id_produto
) af ON p.id_produto = af.id_produto

            WHERE c.nome_categoria IN ('Eletrônicos', 'Roupas')
            GROUP BY
                p.id_produto,
                p.nome_produto,
                c.nome_categoria,
                f.nome_fornecedor,
                e.quantidade_em_estoque,
                s.nome_temporada,
                fore.quantidade_forecast,
                re.quantidade
            ORDER BY p.id_produto;
        """
        
        # Executando a query
        cursor.execute(query)
        
        # Salvando os resultados em uma variável
        linhas = cursor.fetchall()
        logger.info(f"{len(linhas)} registros recuperados do banco.")
        return linhas
    
    except Exception as e:
        logger.error(f"Erro ao consultar dados no SQLite: {str(e)}")
        raise
    
    finally:
        try:
            # Fechando a conexão com o banco
            conn.close()
            logger.info("Conexão com SQLite encerrada.")
        except Exception:
            pass
    
def gerar_insights():
    logger.info("Iniciando geração de insights com batch de prompts.")
    
    try:
        linhas = buscar_dados()
        if not linhas:
            logger.warning("Nenhum dado encontrado para processamento.")
            return []

        # Template do prompt
        prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Você é um cientista de dados especialista em previsão de demanda e gestão de estoque.

            Avalie os dados considerando:
            - Volume de vendas
            - Estoque atual
            - Sazonalidade
            - Quantidade prevista (forecast)
            - Qualidade da previsão, usando métricas como MAE e MAPE

            Regras importantes:
            - Se o MAPE for alto, destaque baixa confiabilidade da previsão
            - Evite recomendações agressivas quando a previsão for pouco confiável
            - Priorize decisões conservadoras em cenários de alto erro
            - Gere recomendações práticas para o negócio
            """
        ),
        ("user", "{question}")
    ]
)


        # Concatenando prompt + llm + resposta
        chain = prompt | llm | output_parser
        # Lista para armazenar as respostas do LLM
        insights = []

        for idx, batch in enumerate(criar_batches(linhas, batch_size),start=1):
            logger.info(f"Processando batch {idx} com {len(batch)} produtos.")
            
            try:
                texto_batch = ""
        
                # Loop percorrendo os resultados da consulta para passar as info para o LLM
                for linha in batch:
                    (
                        id_produto,
                        nome_produto,
                        nome_categoria,
                        nome_fornecedor,
                        total_vendido,
                        quantidade_em_estoque,
                        temporada,
                        quantidade_forecast,
                        quantidade_reabastecida,
                        mae,
                        mape
                    ) = linha

                texto_batch += (
                    f"ID_Produto {id_produto}, "
                    f"Nome_Produto {nome_produto}, "
                    f"Categoria {nome_categoria}, "
                    f"Fornecedor {nome_fornecedor}, "
                    f"Total_Vendido {total_vendido}, "
                    f"Estoque {quantidade_em_estoque}, "
                    f"Temporada {temporada}, "
                    f"Forecast {quantidade_forecast}, "
                    f"Reabastecido {quantidade_reabastecida}, "
                    f"Erro absoluto médio: {mae}, "
                    f"Erro absoluto percentual médio: {mape}."
                )
                # Obtendo a resposta do llm
                resposta = chain.invoke({"question" : texto_batch})
                # Inserindo as respostas na lista de respostas
                insights.append(resposta)
                logger.info(f"Batch {idx} processado com sucesso.")
                
            except Exception as e:
                logger.error(f"Erro ao processar batch {idx}: {str(e)}")
                continue  # não derruba o pipeline inteiro
    
        salvar_insights_csv(insights)
        logger.info("Processo de geração de insights finalizado.")
    
        return insights

    except Exception as e:
        logger.critical(f"Falha crítica no pipeline de insights: {str(e)}")
        raise
    
def salvar_insights_csv(insights):
    try:
        logger.info(f"Salvando insights em arquivo CSV: {nome_arquivo(analise)}")
        with open(analise, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Insight"])
            for insight in insights:
                writer.writerow([insight])
    except Exception as e:
        logger.error(f"Erro ao salvar arquivo CSV: {str(e)}")
        raise

# Execução
if __name__ == "__main__":
    gerar_insights()