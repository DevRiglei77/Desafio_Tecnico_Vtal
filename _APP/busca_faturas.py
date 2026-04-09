import imaplib
from dotenv import load_dotenv
import email
import os
import base64
from utils import *
import sys
from config import *

logger = logging.getLogger(__name__)

load_dotenv()
email_ = os.getenv('email')
senha = os.getenv('senha')


def conecta_email():

    try:
        # Instancia o objeto de conexão e indicia o servidor (no caso gmail)
        conecta_email = imaplib.IMAP4_SSL("imap.gmail.com")

        # conecta ao email, passando email e senha
        status, mensagem = conecta_email.login(email_, senha)

        if status == "OK":
            logger.info("Conexão com o email estabelecida com sucesso.")
            conecta_email.list()
            conecta_email.select(mailbox='inbox', readonly=True)
            respostas, idemails = conecta_email.search(None, filtro)
            baixa_anexos(conecta_email,idemails)

    except imaplib.IMAP4.error as e:
        logger.info(f"Falha na autenticação: {e}")
        logger.info(f"Processo encerrado por falta de conexão")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Erro inesperado durante o processo de varredura dos e-mails: {e}")
        sys.exit(1)


def limpar_nome_arquivo(nome):
    return "".join(c for c in nome if c.isalnum() or c in (' ', '.', '_')).rstrip()

#parte é o binario do arquivo, ele será usado para reconstruir o arquivo anexado
def reconstroe_arquivo(parte):

    try:
        nm_arquivo = parte.get_filename()
        nm_arquivo = limpar_nome_arquivo(nm_arquivo)
        caminho_completo = os.path.join(caminho_anexos, nm_arquivo)
        nm_arquivo = os.path.basename(nm_arquivo)
        with open(caminho_completo, "wb") as f:
            f.write(parte.get_payload(decode=True))
            logger.info(f"Fatura baixada com sucesso: {nm_arquivo}")

    except Exception as e:
        logger.error(f"Ocorreu um erro ao baixar o arquivo: {nm_arquivo} - {e}")
        raise

def baixa_anexos(conexao,idemails):

    try:
        for id_email in idemails[0].split():
            resposta,dados = conexao.fetch(id_email,'(RFC822)')
            texto_email = dados[0][1]
            texto_email = texto_email.decode('utf-8')
            texto_email = email.message_from_string(texto_email)
            for parte in texto_email.walk():
                if parte.get_content_maintype() == 'multipart':
                    continue
                if parte.get('Content-Disposition') is None:
                    continue
                if parte.get_filename().lower().endswith('.pdf'):
                    reconstroe_arquivo(parte)

    except Exception as e:
        logger.error(f"Erro Inesperado durante o processo de baixar anexos: {e}")
        raise


