import openai
from PyPDF2 import PdfReader
from config import caminho_anexos
import os
from openai import OpenAI
from dotenv import load_dotenv
from utils import montar_prompt_extracao
from sap_api import criar_ordem_de_compra
import logging


logger = logging.getLogger(__name__)
load_dotenv()
API_KEY = os.getenv('API_KEY_CHATGPT')


cliente = openai.OpenAI(api_key=os.getenv('API_KEY_CHATGPT'))

conteudo = []


def extrair_campos(prompt):

    logger.info("Chamando a Api do chatgpt para a extração de dados")
    try:
        response = cliente.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente que extrai dados de faturas."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )
        content = response.choices[0].message.content.strip()

        if content:
            logger.info("Dados Extraidos com sucesso")
            return content
        else:
            logger.warning("Consulta à API (Openai) não retornou conteúdo.")
            return None

    except Exception as e:
        logger.error("Erro ao consultar a API (Openai): %s", e, exc_info=True)
        raise



def abre_pdf(caminho):

    try:
        reader = PdfReader(caminho)
        nm_arquivo = os.path.basename(caminho)
        numero_paginas = len(reader.pages)

        for i in range(numero_paginas):
            pagina = reader.pages[i]
            texto = pagina.extract_text()
            conteudo.append({"Fatura":nm_arquivo,"Texto":texto,"Pagina":i})

    except Exception as e:
        logger.error(f"Ocorreu um erro inesperado durante o processo de abertura do pdf: {e}")
        raise


def extrair_e_criar_ordem_compra():
    try:
        while len(conteudo) != 0:
            prompt = montar_prompt_extracao(conteudo)
            resposta = extrair_campos(prompt)
            if resposta:
                ordem_compra = criar_ordem_de_compra(resposta)
    except Exception as e:
        raise



def lista_pasta_anexos():

    try:
        if os.path.isdir(caminho_anexos):
            pasta = os.listdir(caminho_anexos)
            for arquivo in pasta:
                nm_arquivo = os.path.join(caminho_anexos,arquivo)
                abre_pdf(nm_arquivo)
    except Exception as e:
        logger.error(f"Erro durante a listagem dos arquivos:{e}")

