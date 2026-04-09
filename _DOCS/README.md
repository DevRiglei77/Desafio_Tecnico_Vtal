### main.py
### Criado por Riglei Marcos ###

# 💼 Automação de Faturas de Energia com Criação de Purchase Orders no SAP (Simulado)

## 📌 Descrição do Projeto

Este projeto automatiza o processo de varredura de e-mails e download de anexos com faturas de energia elétrica, extração de informações essenciais e criação de Purchase Orders (POs) no SAP S/4HANA via uma API REST simulada.

O objetivo é eliminar tarefas manuais do time financeiro, garantindo agilidade, padronização e redução de erros.

---

## 🚀 Funcionalidades

- Simulação da leitura de e-mails com anexos PDF.
- Extração simulada de dados como:
  - CNPJ da concessionária
  - Número do contrato
  - Valor da fatura
  - Data de vencimento
- Criação automatizada de uma PO via API HTTP POST (simulada).
- Log de eventos para acompanhamento da execução.
- Estrutura modular com boas práticas de organização e tratamento de erros.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

| Biblioteca              | Finalidade                                             |
|-------------------------|--------------------------------------------------------|
| `imaplib`/`imap_tools`  | (Simulado) leitura de e-mails via protocolo IMAP       |
| `PyPDF2`/`PdfReader`    | (Simulado) extração de dados de PDFs                   |
| `openai`/`OpenAI`       | Api (llm) que realiza a extração dos dados solicitados |
| `requests`              | Simulação da chamada POST para o SAP API               |
| `logging`               | Geração de logs estruturados                           |
| `os`, `json`            | Manipulação de arquivos e estrutura                    |
| `dotenv`/`load_dotenv`  | Carregar variaveis de ambientes                        |
| `base64`                | Decodificar no padrão utf-8 os emails                  |
| `sys`                   | Interromper o processo em caso de algum erro           |
| `datetime`              | Manipulação de data e hora para o filtro dos emails    |

---

___

### Fluxo do projeto

  1) Busca dos arquivos com anexos - busca_faturas.py
     ## O script main.py chama a função conecta_email() localizada no 
     ## arquivo busca_faturas.py, que por sua vez conecta_email() busca as variavies
     ## email e senha que estão no arquivo .env para realizar a conexão..
     ## Se o status do metodo conecta_email.login(email_, senha)  for ok, ele segue com o fluxo e aplica o filtro
     ## que busca emails cujo o assunto tenha fatura ou conta e que foi enviado entre o primeiro
     ## dia do mês passado até o dia vigente.
     ## Após isso, conecta_email() chama a função baixa_anexos(conecta_email,idemails),
     ## que por sua vez percorre todos os emails retornados pelo filtro, 
     ## procurando anexo (pdf), se caso o email tiver anexo a função 
     ## reconstroe_arquivo(parte) é chamada para criar o arquivo e salvar na pasta _ANEXOS

  2) Listagem da Pasta _ANEXOS
     ## Após a varredura dos emails e a busca por anexos,
     ## o arquivo main.py chama a função lista_pasta_anexos() 
     ## localizada no arquivo extrai_dados_pdf.py.
     ## por sua vez essa função citada percorre todos os
     ## arquivos que foram salvos na pasta _ANEXOS e chama a função abre_pdf().
     ## Que por sua vez abre o pdf e extrai o texto salvado em um dicionario 
     ## com a seguinte estrutura {"Fatura":nm_arquivo,"Texto":texto,"Pagina":i}}.

  3) Extração de Dados Relevantes e Criação de Ordem de Compra
  ## Após a abertura e extração dos dados o script main.py
  ## chama a função extrair_e_criar_ordem_compra() que percorre o dicionario
  ## onde os dados das faturas estão salvos, a cada interação a função
  ## montar_prompt_extracao(conteudo) é chamada para montar o prompt para llm e
  ## garantir que o prompt não ultrapasse 40mil caracteres por requisição.
  ## Se caso o script prevê que esse limite será ultrapassado, uma requisição é feita
  ## e o restante das faturas são passadas a llm em outro lote.
  ## Ao fazer a requisição a llm, os dados relevantes são extraídos e retornado um JSON
  ## que esse mesmo é passado para a função criar_ordem_de_compra(po_data).
  ## essa função tem como por objetivo realizar a integração com o sap e criar uma
  ## ordem de compra.

---

## 📁 Estrutura do Projeto

```bash
Desafio_Tecnico
    .Venv
    _ANEXOS                             #Pasta aonde os arquivos irão ficar salvos
    _APP                                #Pasta aonde ficam os scripts python
        ├── .env                        # Arquivo aonde ficam as variaveis sensiveis de ambientes  
        ├── main.py                     # Arquivo principal da automação        
        ├── buscar_faturas.py           # Arquivo responsavel por conectar e baixar as faturas do email        
        ├── extrai_dados.py             # Arquivo responsavel por ler e extrair dados do pdf
        ├── sap_api.py                  # Arquivo responsavel por intregrar por fazer a integração com o sap e criar uma ordem de compra
        ├── utils.py                    # Arquivo que tem funções uteis para o projeto
        ├── config.py                   # Arquivo aonde é setado as variaveis que serão usadas em outros arquivos.py
        ├── requirements.txt            # Arquivos com todas as depedencias do projeto

    _LOGS
             ├── app.log                #Arquivo aonde fica guardado o log do processo
    
    _DOCS
             ├── READ.ME    


## Configuração do Ambiente

1. **Criação do Ambiente Virtual**:
Navegue até a pasta *_APP* pelo **POWERSHELL** e digite os seguintes comandos:

```sh
python -m venv venv
```

2. **Ativação do Ambiente Virtual**:

No Windows:
```sh
.\venv\Scripts\activate
```

No macOS/Linux:
```sh
source venv/bin/activate
```

Instalação das Dependências:
Certifique-se de que o ambiente virtual esteja ativado e execute:

```sh
pip install -r _APP/requirements.txt
```

3. **Configuração do Projeto**
Configuração do Arquivo .env:
Adicione as seguintes variáveis ao arquivo .env:

email<No caso precisa ser gmail>
senha<senha do email>
SAP_API_URL<Chave da api do sap>
API_KEY_CHATGPT<Chave da api do chatgpt>


4. **Exemplo para rodar o projeto**

python _APP/main.py

```bash OBS: Criar um arquivo .env para colocar todos os seus dado sensiveis, conforme mencionado
            