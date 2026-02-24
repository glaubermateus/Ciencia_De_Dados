import os
from pathlib import Path
from logging_config import setup_logger

# Diretorio principal
base_dir = Path(__file__).resolve().parents[1]

# pastas
dados_origem = os.path.join(base_dir, 'datasets')
output = os.path.join(base_dir, 'output')
# Criar a pasta output caso não exista
os.makedirs(output, exist_ok=True)

# arquivos
banco = os.path.join(output, 'vendas.db')
analise = os.path.join(output,'analise.csv')
filename = os.path.join(base_dir,"scripts\\1-tabelas.sql")

print(filename)

config_tabelas = {
    "fornecedores": {
        "arquivo": "fornecedores.csv",
        "colunas_obrigatorias": ["id_fornecedor", "nome_fornecedor", "nome_contato", "email_contato"]
    },
    "categorias": {
        "arquivo": "categorias.csv",
        "colunas_obrigatorias": ["id_categoria", "nome_categoria"]
    },
    "produtos": {
        "arquivo": "produtos.csv",
        "colunas_obrigatorias": ["id_produto", "nome_produto", "id_categoria", "id_fornecedor","preco_unitario"]
    },
    "clientes": {
        "arquivo": "clientes.csv",
        "colunas_obrigatorias": ["id_cliente", "nome_cliente", "email"]
    },
    "vendas": {
        "arquivo": "vendas.csv",
        "colunas_obrigatorias": ["id_venda", "id_produto", "id_cliente", "data_venda", "quantidade_vendida", "total_venda"]
    },
    "estoque": {
        "arquivo": "estoque.csv",
        "colunas_obrigatorias": ["id_estoque", "id_produto", "quantidade_em_estoque", "data_ultimo_reabastecimento"]
    },
    "sazonalidade": {
        "arquivo": "sazonalidade.csv",
        "colunas_obrigatorias": ["id_sazonalidade", "id_produto", "nome_temporada", "data_inicio","data_fim"]
    },
    "forecast": {
        "arquivo": "forecast.csv",
        "colunas_obrigatorias": ["id_forecast", "id_produto", "data_forecast", "quantidade_forecast"]
    },
    "reabastecimento": {
        "arquivo": "reabastecimento.csv",
        "colunas_obrigatorias": ["id_reabastecimento", "id_produto", "data_reabastecimento", "quantidade"]
    },
    "pedidos": {
        "arquivo": "pedidos.csv",
        "colunas_obrigatorias": ["id_pedido", "id_fornecedor", "data_pedido", "id_produto","quantidade"]
    }
}

# objeto logger
logger = setup_logger(pasta_log=os.path.join(base_dir,"logs"))

# scripts
cria_tabelas = os.path.join(base_dir,"scripts\\2-cria_tabelas.py")
carrega_dados = os.path.join(base_dir,"scripts\\3-carrega_dados.py")
llm = os.path.join(base_dir,'scripts\\4-llm.py')