import mysql.connector
import csv
from datetime import datetime, timedelta
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
#///////////////////////////////////////////////
#=================Conexoes============================
MYSQL_BANCO_DE_DADOS = "========="
MYSQL_SERVIDOR = "========="
MYSQL_USUARIO = "$========="
MYSQL_SENHA = "$==========="
#===============================================
# Config GitLab
GITLAB_URL = "========="
GITLAB_ID_USUARIO = "user_id"  # ID GitLab
GITLAB_TOKEN = "glpat-kHJXvuTqY2sUNRBQ3a_Z"  # criar Token permanente
#========================================================================
# Configu do email
EMAIL_ORIGEM = "========="  # / criar um Email para a aplicação
EMAIL_DESTINO = "=========="
SENHA_EMAIL = "============="
#//////////////////////////////////////////////////////////////////
# Consulta SQL para encontrar lojas indisponíveis nos últimos 30 dias com detalhes de tempo
SQL_CONSULTA = """
SELECT 
    h.nome AS loja, 
    FROM_UNIXTIME(e.clock) AS inicio_indisponibilidade, 
    FROM_UNIXTIME(e.clock + e.valor) AS fim_indisponibilidade, 
    (e.clock + e.valor) - e.clock AS duracao_segundos, 
    SEC_TO_TIME((e.clock + e.valor) - e.clock) AS duracao_formatada 
FROM 
    eventos e 
JOIN 
    hospedeiros h ON e.objeto_id = h.id 
WHERE 
    e.origem = '0' 
    AND e.objeto = '0' 
    AND e.valor = '1' 
    AND h.nome LIKE 'FastShop%' 
    AND e.clock > UNIX_TIMESTAMP(DATE_SUB(NOW(), INTERVAL 30 DAY)) 
ORDER BY 
    h.nome, inicio_indisponibilidade;
"""

# Função para executar a consulta SQL
def executar_consulta_sql():
    conexao = None
    try:
        conexao = mysql.connector.connect(
            host=MYSQL_SERVIDOR,
            user=MYSQL_USUARIO,
            password=MYSQL_SENHA,
            database=MYSQL_BANCO_DE_DADOS
        )
        cursor = conexao.cursor()

        # Executa a consulta SQL
        cursor.execute(SQL_CONSULTA)
        resultados = cursor.fetchall()

        return resultados

    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None
    
    finally:
        if conexao and conexao.is_connected():
            cursor.close()
            conexao.close()
            print("Conexão ao MySQL encerrada.")

# Função para formatar os dados em CSV
def formatar_para_csv(resultados):
    if not resultados:
        return None
    
    dados_csv = []
    headers = ['Loja', 'Inicio_Indisponibilidade', 'Fim_Indisponibilidade', 'Duracao_Segundos', 'Duracao_Formatada']
    dados_csv.append(headers)

    for linha in resultados:
        dados_csv.append(linha)

    return dados_csv

# Função para enviar o arquivo CSV por email
def enviar_por_email(dados_csv):
    try:
        # Criar mensagem
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO
        msg['Subject'] = "Relatório de Lojas Indisponíveis"

        # Corpo da mensagem
        corpo_email = """
        Prezado usuário,

        Em anexo está o relatório de lojas indisponíveis nos últimos 30 dias.

        Atenciosamente,
        Seu Nome
        """
        msg.attach(MIMEText(corpo_email, 'plain'))

        # Anexar arquivo CSV
        csv_data = "\n".join([",".join(map(str, linha)) for linha in dados_csv])
        arquivo_csv = MIMEBase('application', 'octet-stream')
        arquivo_csv.set_payload(csv_data.encode())
        encoders.encode_base64(arquivo_csv)
        arquivo_csv.add_header('Content-Disposition', 'attachment', filename='resultados.csv')
        msg.attach(arquivo_csv)

        # Enviar email usando SMTP
        servidor_smtp = smtplib.SMTP('smtp.gmail.com', 587)
        servidor_smtp.starttls()
        servidor_smtp.login(EMAIL_ORIGEM, SENHA_EMAIL)
        texto_email = msg.as_string()
        servidor_smtp.sendmail(EMAIL_ORIGEM, EMAIL_DESTINO, texto_email)
        servidor_smtp.quit()

        print("Email enviado com sucesso!")

    except Exception as e:
        print(f"Erro ao enviar email: {e}")

# Função principal para executar o script
def principal():
    resultados = executar_consulta_sql()
    dados_csv = formatar_para_csv(resultados)

    if dados_csv:
        enviar_por_email(dados_csv)

if __name__ == "__main__":
    principal()
