# Imports
from config import logger, filename
from utils import conectar_banco

# Criar tabelas no banco no banco
def criar_tabelas(filename):
    conn  = conectar_banco()
    cur = conn.cursor()
    
    # Lê o conteúdo do arquivo SQL
    try:
        logger.info("Iniciando a leitura do arquivo sql.")
        with open(filename, 'r') as file:
            sql_script = file.read()
    except Exception as e:
        logger.error(f"Erro ao ler o arquivo sql: {e}")
        raise
    
    try:
        logger.info("Criando tabelas...")
        # Executa o script SQL
        cur.executescript(sql_script)
        # Confirma as mudanças no banco de dados
        conn.commit()  
        logger.info("Script executado com sucesso!")
    except Exception as e:
        # Reverte as mudanças em caso de erro
        conn.rollback()  
        logger.error(f"Erro ao executar o script: {e}")
        raise
    finally:
        # Fecha a comunicação com o banco de dados
        cur.close()
        conn.close()

# Chamando a função
if __name__ == "__main__":
    criar_tabelas(filename)