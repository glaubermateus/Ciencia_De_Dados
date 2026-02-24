# Imports
import subprocess
from utils import nome_arquivo
from config import logger, cria_tabelas, carrega_dados, llm

# Função para executar outros scripts Python
def run_pipeline(script_name):
    try:
        result = subprocess.run(['python', script_name], check=True, capture_output=True, text=True)
        final = f"Script {nome_arquivo(script_name)} executado com sucesso."
        logger.info(final)
    except subprocess.CalledProcessError as e:
        final = f"Erro ao executar o script {nome_arquivo(script_name)}."
        logger.error(final)

# Dicionário de scripts
scripts = {
"cria_tabelas.py": cria_tabelas,
"carrega_dados.py": carrega_dados,
"llm.py": llm
}

# Executa os scripts em um loop
for chave, valor in scripts.items():
    logger.info(f"Iniciando a execução de: {chave}!")
    run_pipeline(valor)
    logger.info(f"Termino da execução de: {chave}!")

logger.info("Pipeline executado.")
print("Pipeline executado.")