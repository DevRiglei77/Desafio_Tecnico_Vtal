import os
import logging
from config import caminho_pasta_log,caminho_arq_log,prompt_final,prompt_inicio

def configura_arq_log():
    try:
        os.makedirs(caminho_pasta_log, exist_ok=True)

        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        logging.basicConfig(
            filename=os.path.join(caminho_pasta_log, "app.log"),
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            encoding="utf-8"
        )
    except Exception as e:
        raise e

def deletar_log():

    try:
        if os.path.exists(caminho_arq_log):
            os.remove(caminho_arq_log)
    except Exception as e:
        logging.error(f"Erro ao deletar o log: {e}")
        raise

def verifica_limite_caracter(fatura,texto,pagina,prompt):

    try:
        max_carater = 40000
        total_caracter = fatura + texto + pagina + prompt + len(prompt_final)
        if total_caracter > max_carater:
            return 1
    except Exception as e:
        raise

def apaga_indices(lista,conteudo):
    try:
        lista.sort(reverse=True)
        for indice in lista:
            conteudo.pop(indice)
    except Exception as e:
        raise

def montar_prompt_extracao(conteudo):

    prompt = prompt_inicio
    indice_remover = []

    try:
        for indice,item in enumerate(conteudo):
            prompt += f"""
                ### Fatura: {item['Fatura']}
                Página: {item['Pagina']}
                Texto:  {item['Texto']}
            ---"""

            indice_remover.append(indice)
            if len(conteudo) - 1 >= indice + 1:
                tam_fatura = len(conteudo[indice + 1]['Fatura'])
                tam_pagina = len(str(conteudo[indice + 1]['Pagina']))
                tam_texto =  len(conteudo[indice + 1]['Texto'])
                tam_prompt = len(prompt)
                if verifica_limite_caracter(tam_fatura,tam_texto,tam_pagina,tam_prompt) == 1:
                    prompt += prompt_final
                    apaga_indices(indice_remover,conteudo)
                    return prompt

        prompt+=prompt_final
        apaga_indices(indice_remover,conteudo)

    except Exception as e:
        logging.error(f"Falha na montagem do prompt para a API: {e}")
        raise

    return prompt
