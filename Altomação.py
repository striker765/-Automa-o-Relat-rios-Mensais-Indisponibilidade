import mysql.connector
import csv
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import os
from config import MYSQL_CONFIG, EMAIL_CONFIG, FILE_CONFIG

# Configurações do MySQL
MYSQL_BANCO_DE_DADOS = MYSQL_CONFIG['database']
MYSQL_HOST = MYSQL_CONFIG['host']
MYSQL_USUARIO = MYSQL_CONFIG['user']
MYSQL_SENHA = MYSQL_CONFIG['password']

# Configurações do Outlook
EMAIL_USUARIO = EMAIL_CONFIG['username']
EMAIL_SENHA = EMAIL_CONFIG['password']
EMAIL_REMETENTE = EMAIL_CONFIG['sender']
EMAIL_DESTINATARIOS = EMAIL_CONFIG['recipients']

# Configurações do servidor SMTP do Outlook
SMTP_SERVIDOR = EMAIL_CONFIG['smtp_server']
SMTP_PORTA = EMAIL_CONFIG['smtp_port']

# Arquivos de log
ARQUIVO_LOG = FILE_CONFIG['log_file']
ARQUIVO_CSV = FILE_CONFIG['csv_file']

# Consulta SQL para coletar uso de CPU dos últimos 30 dias do host especificado
CONSULTA_SQL = """
SHOW TABLES;
"""

# Função para escrever logs
def escrever_log(mensagem):
    with open(ARQUIVO_LOG, 'a') as arquivo_log:
        arquivo_log.write(f"{datetime.now()} - {mensagem}\n")

# Função para executar a consulta SQL
def executar_consulta_sql():
    conexao = None
    try:
        conexao = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USUARIO,
            password=MYSQL_SENHA,
            database=MYSQL_BANCO_DE_DADOS
        )
        cursor = conexao.cursor()
        cursor.execute(CONSULTA_SQL)
        resultados = cursor.fetchall()
        return resultados

    except mysql.connector.Error as erro:
        mensagem_erro = f"Erro ao conectar ao MySQL: {erro}"
        escrever_log(mensagem_erro)
        enviar_email(assunto='Erro na Execução do Script', corpo=mensagem_erro, log_file=ARQUIVO_LOG)
        return None

    finally:
        if conexao and conexao.is_connected():
            cursor.close()
            conexao.close()
            escrever_log("Conexão ao MySQL encerrada.")

# Função para formatar os dados em CSV
def formatar_para_csv(resultados):
    if not resultados:
        return None

    dados_csv = []
    # Cabeçalhos das colunas
    cabecalhos = ['host', 'inicio_coleta', 'fim_coleta', 'duracao_segundos', 'duracao_formatada']
    dados_csv.append(cabecalhos)

    for linha in resultados:
        # Adiciona cada linha de resultados ao CSV
        dados_csv.append(linha)

    return dados_csv

# Função para salvar o arquivo CSV
def salvar_csv(dados_csv):
    if not dados_csv:
        return

    try:
        with open(ARQUIVO_CSV, 'w', newline='') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerows(dados_csv)
        escrever_log(f"Arquivo CSV salvo em {ARQUIVO_CSV}")
    except IOError as erro:
        mensagem_erro = f"Erro ao salvar o arquivo CSV: {erro}"
        escrever_log(mensagem_erro)
        enviar_email(assunto='Erro ao Salvar CSV', corpo=mensagem_erro, log_file=ARQUIVO_LOG)

# Função para enviar o e-mail
def enviar_email(assunto, corpo, log_file=None, anexos=[]):
    try:
        # Ler conteúdo do arquivo de log se existir
        if log_file and os.path.exists(log_file):
            with open(log_file, 'r') as file:
                log_content = file.read()
            corpo = f"{corpo}\n\nLog:\n{log_content}"

        # Criar mensagem MIME
        mensagem = MIMEText(corpo)
        mensagem['From'] = EMAIL_REMETENTE
        mensagem['To'] = ', '.join(EMAIL_DESTINATARIOS)
        mensagem['Subject'] = assunto

        # Conectar ao servidor SMTP
        with smtplib.SMTP(SMTP_SERVIDOR, SMTP_PORTA) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_USUARIO, EMAIL_SENHA)
            smtp.sendmail(EMAIL_REMETENTE, EMAIL_DESTINATARIOS, mensagem.as_string())
            escrever_log(f"Email enviado com sucesso: {assunto}")

    except Exception as erro:
        mensagem_erro = f"Erro ao enviar email: {erro}"
        escrever_log(mensagem_erro)

# Função principal para executar o script
def principal():
    escrever_log("Início da execução do script.")

    resultados = executar_consulta_sql()
    if resultados:
        dados_csv = formatar_para_csv(resultados)
        salvar_csv(dados_csv)
        enviar_email(
            assunto='Resultados da Coleta SQL',
            corpo='Segue em anexo o arquivo CSV com os resultados da coleta SQL.',
            anexos=[ARQUIVO_CSV]
        )

    escrever_log("Execução do script concluída.")

if __name__ == "__main__":
    principal()
