Desafio Técnico – Automação para Criação de PO no SAP S/4HANA

Cenário
O time financeiro da empresa recebe mensalmente dezenas de faturas de
energia elétrica por e-mail. Hoje, o processo para iniciar o pagamento é
totalmente manual:
1. O analista abre cada e-mail, identifica os anexos PDF com as faturas e
extrai informações como:
o CNPJ da concessionária
o Número do contrato
o Valor total da fatura
o Data de vencimento
2. Com esses dados, ele acessa o SAP S/4HANA e cria uma Purchase Order
(PO) para iniciar o fluxo de pagamento.
Queremos automatizar esse processo com Python, garantindo agilidade, redução
de erros e padronização.

O desafio
Desenvolva uma automação em Python que:
1. Acesse uma caixa de e-mail (IMAP ou API) e identifique mensagens com
faturas de energia elétrica em anexo (PDF). (Não é necessário um acesso real –
simule)
2. Extraia dos anexos os seguintes dados (não é necessário uma extração
real – simule):
• CNPJ da concessionária
• Número do contrato
• Valor total da fatura
• Data de vencimento

PÚBLICA

3. Crie automaticamente uma PO no SAP S/4HANA consumindo uma API
REST simulada (não é necessário acesso ao SAP real – simule a chamada HTTP).
4. Implemente boas práticas de código, incluindo:
• Estrutura modular e organizada (separação em funções e/ou classes).
• Tratamento de erros e logs.
• Documentação para facilitar manutenção e entendimento.

🛠 Requisitos técnicos
• Use Python 3.
• Utilize bibliotecas adequadas para cada etapa:
o Leitura de e-mails: imaplib, imap_tools ou API (ex.: Microsoft Graph).
o Processamento de PDFs: pdfplumber, PyPDF2 ou pytesseract (se
OCR for necessário).
o Consumo de API REST: requests.
• Simule a API do SAP com uma chamada HTTP POST para o endpoint
https://sap-api.fake/purchase-orders.

Entrega
O candidato deve enviar os seguintes arquivos em um .zip:
1. Código-fonte:
• Scripts Python organizados em pastas se necessário.
• Nomeie o arquivo principal como main.py.
2. README.md (obrigatório):
• Explique como rodar o projeto (dependências e instruções).
• Descreva o fluxo da automação.
• Liste as bibliotecas usadas e por quê.
3. (Obrigatório) – Inclua um arquivo requirements.txt com as dependências do
projeto.

PÚBLICA

Critérios de avaliação
Critério Peso
Lógica da solução e clareza do fluxo
Organização e boas práticas do código
Uso correto de bibliotecas Python
Tratamento de erros e logs
Documentação (README.md)
Criatividade para lidar com limitações

Observações
• Não precisa implementar uma solução 100% funcional com autenticação
real ou credenciais do SAP. Pode simular a API com chamadas HTTP.
• Foco na estrutura e clareza do código.
