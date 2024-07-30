Coleta de Dados SQL e Envio por Email
Este script Python foi desenvolvido para conectar-se a um banco de dados MySQL, executar uma consulta SQL, formatar os resultados em um arquivo CSV e enviar esses resultados por email usando um servidor SMTP configurado.

Funcionalidades
Conexão ao banco de dados MySQL para executar consultas SQL.
Formatação dos resultados da consulta em um arquivo CSV.
Envio automático por email do arquivo CSV gerado como anexo.
Registro de logs para monitorar a execução do script e capturar erros.
Requisitos
Para executar este script, você precisará ter instalado:

Python 3.x
Bibliotecas Python:
mysql-connector-python: Para conectar ao MySQL.
smtplib: Para enviar emails.
Configuração
Arquivo config.py:

Crie um arquivo config.py na raiz do projeto com as seguintes variáveis configuradas:

python
Copiar código
# Configurações do MySQL
MYSQL_CONFIG = {
    'host': 'seu_host_mysql',
    'database': 'seu_banco_de_dados',
    'user': 'seu_usuario_mysql',
    'password': 'sua_senha_mysql'
}

# Configurações do servidor SMTP (Outlook, Gmail, etc.)
EMAIL_CONFIG = {
    'smtp_server': 'smtp.servidor.com',  # servidor SMTP
    'smtp_port': 587,                    # porta do servidor SMTP
    'username': 'seu_email@example.com',
    'password': 'sua_senha_de_email',
    'sender': 'seu_email@example.com',   # remetente do email
    'recipients': ['destinatario1@example.com', 'destinatario2@example.com']  # lista de destinatários
}

# Arquivos de log e CSV
FILE_CONFIG = {
    'log_file': 'arquivo_de_log.txt',
    'csv_file': 'resultado_consulta.csv'
}
Substitua os valores dentro de cada dicionário (MYSQL_CONFIG, EMAIL_CONFIG, FILE_CONFIG) pelos seus próprios detalhes de configuração.

Instalação de Dependências:

Para instalar as bibliotecas necessárias, use o pip:

bash
Copiar código
pip install mysql-connector-python
bash
Copiar código
pip install secure-smtplib
Utilização
Para executar o script, use o seguinte comando no terminal:

bash
Copiar código
python main.py
O script realizará a consulta SQL configurada, formatará os resultados em um arquivo CSV e enviará por email aos destinatários especificados em EMAIL_CONFIG.

Logs
Todos os logs da execução do script são registrados no arquivo arquivo_de_log.txt, localizado no diretório do projeto. Verifique este arquivo em caso de erros ou para acompanhar o progresso das execuções.

Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests com melhorias ou correções.

Licença
Este projeto está licenciado sob a MIT License.
