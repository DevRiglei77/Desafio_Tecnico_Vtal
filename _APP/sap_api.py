import requests
from dotenv import load_dotenv
import os
import logging

load_dotenv()
logger = logging.getLogger(__name__)

SAP_API_URL = os.getenv("SAP_API_URL")


def criar_ordem_de_compra(po_data):

    logger.info("Criando ordem de compra no sap")
    try:
        response = requests.post(SAP_API_URL, json=po_data)
        if response.status_code == 201:
            logger.info("PO criada com sucesso!")
            return response.json()
        else:
            logger.error(f"Falha ao criar PO: {response.status_code} - {response.text}")
            return None
    except requests.RequestException as e:
        logger.error(f"Erro na chamada API SAP: {e}")
        return None


