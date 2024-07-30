Coleta de Dados SQL e Envio por Email
Visão Geral
Este script Python foi desenvolvido para realizar consultas SQL em um banco de dados MySQL, formatar os resultados em um arquivo CSV e enviar esses resultados por email usando um servidor SMTP configurado.

Funcionalidades
Conexão ao banco de dados MySQL para executar uma consulta SQL especificada.
Formatação dos resultados da consulta em um arquivo CSV.
Envio automático por email do arquivo CSV gerado como anexo.
Registro de logs para monitorar a execução do script e capturar erros.
Requisitos
Para executar este script, você precisará ter instalado:

Python 3.x
Bibliotecas Python:
mysql-connector-python: Para conectar ao MySQL.
smtplib: Para enviar emails.
Além disso, você deve configurar corretamente os arquivos de configuração conforme descrito abaixo.

Configuração
Arquivo config.py:

Dentro do diretório do projeto, crie um arquivo config.py com as seguintes variáveis configuradas:

python
Copiar código
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
Certifique-se de substituir os valores dentro de cada dicionário (MYSQL_CONFIG, EMAIL_CONFIG, FILE_CONFIG) pelos seus próprios detalhes de configuração.

Instalação de Dependências:

Para instalar as bibliotecas necessárias, use o pip:

bash
Copiar código
pip install mysql-connector-python
bash
Copiar código
pip install secure-smtplib
Utilização
Para executar o script, basta executar o arquivo main.py:

bash
Copiar código
python main.py
O script realizará automaticamente a consulta SQL configurada, formatará os resultados em um arquivo CSV e enviará por email aos destinatários especificados em EMAIL_CONFIG.

Logs
Todos os logs da execução do script são registrados no arquivo arquivo_de_log.txt, localizado no diretório do projeto. Verifique este arquivo em caso de erros ou para acompanhar o progresso das execuções.

Melhorias Futuras
Implementação de testes unitários para garantir a robustez do código.
Refatoração para tornar o código mais modular e fácil de manter.
Adição de tratamento de erros mais detalhado para diferentes cenários de falha.

