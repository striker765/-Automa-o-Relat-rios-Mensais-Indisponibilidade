# Coleta de Dados SQL e Envio por Email

Este script Python se conecta a um banco de dados MySQL, executa uma consulta SQL, formata os resultados em um arquivo CSV e envia esses resultados por email usando SMTP.

## Descrição

O projeto visa automatizar o processo de coleta de dados de um banco MySQL, formatação em CSV e envio por email.

## Requisitos

- Python 3.x
- mysql-connector-python
- secure-smtplib

## Configuração

1. Crie um arquivo `config.py` na raiz do projeto conforme o exemplo fornecido.
2. Configure as variáveis dentro de `config.py` com seus próprios detalhes de conexão MySQL e configurações de email.

Exemplo de `config.py`:

```python
MYSQL_CONFIG = {
    'host': 'seu_host_mysql',
    'database': 'seu_banco_de_dados',
    'user': 'seu_usuario_mysql',
    'password': 'sua_senha_mysql'
}

EMAIL_CONFIG = {
    'smtp_server': 'smtp.servidor.com',
    'smtp_port': 587,
    'username': 'seu_email@example.com',
    'password': 'sua_senha_de_email',
    'sender': 'seu_email@example.com',
    'recipients': ['destinatario1@example.com', 'destinatario2@example.com']
}


Instalação
Clone o repositório:
bash
Copiar código
git clone https://github.com/seu-usuario/nome-do-repositorio.git
Navegue até o diretório:
bash
Copiar código
cd nome-do-repositorio
Instale as dependências:
bash
Copiar código
pip install -r requirements.txt
Uso
Para executar o script, use:

bash
Copiar código
python main.py
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests com melhorias ou correções.

Licença
Este projeto está licenciado sob a MIT License.
FILE_CONFIG = {
    'log_file': 'logs/arquivo_de_log.txt',
    'csv_file': 'resultado_consulta.csv'
}
