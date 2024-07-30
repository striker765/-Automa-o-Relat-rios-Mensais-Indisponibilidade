# Coleta Automatizada de Indisponibilidades do Zabbix

Este projeto em Python automatiza a coleta de dados de indisponibilidade do sistema de monitoramento Zabbix. Ele gera um relatório detalhado de 30 dias que documenta todo o período de indisponibilidade de um monitoramento específico.

## Descrição

O objetivo deste script é conectar-se ao banco de dados do Zabbix, executar uma consulta SQL para extrair informações precisas sobre indisponibilidades registradas no sistema, e formatar esses dados em um arquivo CSV estruturado. O arquivo CSV é então enviado automaticamente por email aos destinatários configurados, proporcionando uma visão clara e detalhada do histórico de falhas de monitoramento.

## Funcionalidades

- Conexão segura ao banco de dados do Zabbix usando `mysql-connector-python`.
- Formatação automática dos resultados da consulta em um arquivo CSV.
- Envio automatizado por email do arquivo CSV gerado como anexo usando `smtplib`.
- Registro detalhado de logs para monitoramento da execução do script e captura de erros.

## Requisitos

- Python 3.x
- Bibliotecas Python: `mysql-connector-python`, `secure-smtplib`

## Configuração

1. **Configurações do MySQL (Zabbix)**:

   Configure as variáveis no arquivo `config.py` com os detalhes de conexão ao banco de dados do Zabbix.

   Exemplo de `config.py`:

   ```python
   MYSQL_CONFIG = {
       'host': 'seu_host_zabbix',
       'database': 'nome_banco_zabbix',
       'user': 'seu_usuario_zabbix',
       'password': 'sua_senha_zabbix'
   }

Configurações do Servidor SMTP:

Configure as variáveis no arquivo config.py com os detalhes do servidor SMTP para enviar os relatórios por email.

Exemplo de config.py:

EMAIL_CONFIG = {
    'smtp_server': 'smtp.servidor.com',
    'smtp_port': 587,
    'username': 'seu_email@example.com',
    'password': 'sua_senha_de_email',
    'sender': 'seu_email@example.com',
    'recipients': ['destinatario1@example.com', 'destinatario2@example.com']
}

Arquivos de Log e CSV:

Configure as variáveis no arquivo config.py com os caminhos dos arquivos de log e CSV.

Exemplo de config.py:

FILE_CONFIG = {
    'log_file': 'logs/arquivo_de_log.txt',
    'csv_file': 'resultado_indisponibilidade.csv'
}

Instalação
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/nome-do-repositorio.git
Navegue até o diretório do projeto:

bash
Copiar código
cd nome-do-repositorio
Instale as dependências necessárias:

bash
Copiar código
pip install -r requirements.txt
Uso
Para executar o script e gerar o relatório de indisponibilidade do Zabbix, utilize o seguinte comando:

bash
Copiar código
python main.py
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests com melhorias ou correções.

Licença
Este projeto está licenciado sob a MIT License.
