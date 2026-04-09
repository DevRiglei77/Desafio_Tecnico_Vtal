from datetime import datetime,timedelta
import os



data_atual = datetime.now()
primeiro_dia_mes_passado = (data_atual.replace(day=1) - timedelta(days=1)).replace(day=1)
primeiro_dia_mes_passado = primeiro_dia_mes_passado.strftime("%d-%b-%Y")
caminho_anexos = os.path.join(os.path.dirname(__file__), "..", "_ANEXOS")
filtro = f'(OR SUBJECT "Fatura" SUBJECT "conta") SINCE {primeiro_dia_mes_passado}'
caminho_pasta_log = os.path.join(os.path.dirname(__file__), "..", "_LOGS")
caminho_arq_log = os.path.join(os.path.dirname(__file__), "..", "_LOGS", "app.log")
prompt_final = """
Retorne os dados extraídos no seguinte formato JSON:

[
  {
    "Fatura": "nome_da_fatura.pdf",
    "CNPJ": "XX.XXX.XXX/XXXX-XX",
    "Contrato": "123456",
    "ValorTotal": "R$ 1234,56",
    "Vencimento": "DD/MM/AAAA"
  },
  ...
]
"""


prompt_inicio = """
Você é um assistente especializado em interpretar textos de faturas de energia elétrica extraídos de arquivos PDF. 
Para cada trecho de texto fornecido, extraia com precisão os seguintes campos:

• CNPJ da concessionária  
• Número do contrato  
• Valor total da fatura  
• Data de vencimento  

Se algum campo não estiver presente, responda com "Não encontrado".

Abaixo estão os textos extraídos por página das faturas:

"""

