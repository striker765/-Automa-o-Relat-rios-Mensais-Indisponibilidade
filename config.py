# Configurações do MySQL
MYSQL_CONFIG = {
    'host': 'seu_host_mysql',
    'database': 'seu_banco_de_dados',
    'user': 'seu_usuario_mysql',
    'password': 'sua_senha_mysql'
}

# Configurações do Outlook (ou outro servidor SMTP)
EMAIL_CONFIG = {
    'smtp_server': 'smtp.outlook.com',  # servidor SMTP
    'smtp_port': 587,                   # porta do servidor SMTP
    'username': 'seu_email@outlook.com',
    'password': 'sua_senha_de_email',
    'sender': 'seu_email@outlook.com',  # remetente do email
    'recipients': ['destinatario1@example.com', 'destinatario2@example.com']  # lista de destinatários
}

# Arquivos de log e CSV
FILE_CONFIG = {
    'log_file': 'arquivo_de_log.txt',
    'csv_file': 'resultado_consulta.csv'
}
