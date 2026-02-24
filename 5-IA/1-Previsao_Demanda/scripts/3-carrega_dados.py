# Imports
from utils import conectar_banco
from config import logger, dados_origem, config_tabelas
import pandas as pd
import os

# Validar colunas
def validar_colunas(df, colunas_esperadas, tabela):
    logger.info("Iniciando validação de colunas.")
    colunas_arquivo = df.columns.tolist()
    faltantes = [c for c in colunas_esperadas if c not in colunas_arquivo]
    
    if faltantes:
        erro = f"Tabela {tabela} - colunas ausentes: {faltantes}"
        logger.error(erro)
        raise ValueError(erro)

# Inserir os dados no banco de dados
def carregar_csv_para_tabela(conn, tabela, config):
    arquivo = config["arquivo"]
    colunas_obrigatorias = config["colunas_obrigatorias"]
    caminho = os.path.join(dados_origem, arquivo)

    logger.info(f"Iniciando carga para a tabela '{tabela}'...")
    
    try:
        if not os.path.exists(caminho):
            logger.warning(f"Arquivo não encontrado: {caminho}")
            return

        logger.info(f"Lendo arquivo CSV: {arquivo}")
        df = pd.read_csv(caminho)
        
        # Validação de colunas
        validar_colunas(df, colunas_obrigatorias, tabela)

        # Carga dos dados
        with conn:
            df.to_sql(tabela, conn, if_exists='append', index=False)
        logger.info(f"{len(df)} registros inseridos na tabela {tabela}")

    except Exception as e:
        logger.error(f"Erro ao carregar {arquivo} na tabela {tabela}: {str(e)}")
        raise
    
# Calcular métricas e inserir na tabela do banco de dados
def calcular_avaliacao(conn):
    logger.info("Iniciando cálculo de métricas de forecast.")

    sql_insert = """
    INSERT INTO avaliacao_forecast (
        id_produto,
        nome_produto,
        nome_categoria,
        periodo,
        quantidade_real,
        quantidade_forecast,
        erro_absoluto,
        erro_quadratico,
        erro_percentual
    )
    SELECT
        p.id_produto,
        p.nome_produto,
        c.nome_categoria,
        strftime('%Y-%m-01', v.data_venda) AS periodo,
        SUM(v.quantidade_vendida) AS quantidade_real,
        SUM(f.quantidade_forecast) AS quantidade_forecast,
        ABS(SUM(v.quantidade_vendida) - SUM(f.quantidade_forecast)) AS erro_absoluto,
        (SUM(v.quantidade_vendida) - SUM(f.quantidade_forecast)) *
        (SUM(v.quantidade_vendida) - SUM(f.quantidade_forecast)) AS erro_quadratico,
        CASE
            WHEN SUM(v.quantidade_vendida) = 0 THEN NULL
            ELSE
                ABS(SUM(v.quantidade_vendida) - SUM(f.quantidade_forecast)) * 1.0
                / SUM(v.quantidade_vendida)
        END AS erro_percentual
    FROM produtos p
    JOIN categorias c ON p.id_categoria = c.id_categoria
    LEFT JOIN vendas v ON p.id_produto = v.id_produto
    LEFT JOIN forecast f
        ON p.id_produto = f.id_produto
        AND strftime('%Y-%m', v.data_venda) = strftime('%Y-%m', f.data_forecast)
    GROUP BY
        p.id_produto,
        p.nome_produto,
        c.nome_categoria,
        periodo;
    """

    conn.execute(sql_insert)
    conn.commit()
    logger.info("Métricas de forecast calculadas e salvas com sucesso.")


# Executar a carga de dados
def executa_carga():
    try:
        logger.info("Iniciando a carga de dados...")
        conn = conectar_banco()
        # Loop para percorrer cada tabela
        for tabela, config in config_tabelas.items():
            carregar_csv_para_tabela(conn, tabela, config)

        logger.info("Carga finalizada com sucesso!")
    
    except Exception as e:
        logger.error(f"Erro na carga de dados: {e}")
    
    try:
        calcular_avaliacao(conn)
        # Fechar a conexão com o banco
        conn.close()
        
    except Exception as e:
        logger.critical(f"Erro crítico na avaliação de forecast: {e}")
        conn.rollback()

    finally:
        conn.close()
        logger.info("Conexão encerrada.")

# Chamando a função
if __name__ == "__main__":
    executa_carga()