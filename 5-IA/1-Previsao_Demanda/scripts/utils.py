# Imports
import sqlite3
from config import banco, logger

# Extrair nome do arquivo
def nome_arquivo(caminho):
    reverso = caminho[::-1]
    idx = reverso.find('\\')
    string = reverso[0:idx]
    string = string[::-1]
    return string

# Conectar no banco
def conectar_banco():
    try:
        conn = sqlite3.connect(banco)
        logger.info(f"Conectado ao banco SQLite: {nome_arquivo(banco)}")
        return conn
    except Exception as e:
        logger.error(f"Erro ao conectar no banco: {str(e)}")
        raise