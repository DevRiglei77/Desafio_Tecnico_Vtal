from busca_faturas import conecta_email
from extrai_dados_pdf import lista_pasta_anexos,extrair_e_criar_ordem_compra
from utils import configura_arq_log,deletar_log
import logging
import os
from config import caminho_anexos


os.makedirs(caminho_anexos, exist_ok=True)
deletar_log()
configura_arq_log()
logger = logging.getLogger(__name__)

def main():
    try:
        logger.info("Iniciando automação de faturas...")
        conecta_email()
        logger.info("Listando Arquivos na pasta _ANEXOS")
        lista_pasta_anexos()
        extrair_e_criar_ordem_compra()
        logger.info("Processo Finalizado")

    except Exception as e:
        pass

if __name__ == "__main__":
    main()