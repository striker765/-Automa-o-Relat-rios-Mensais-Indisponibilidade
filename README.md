📊 Automação de Relatórios Mensais de Indisponibilidade de Lojas

Descrição:
Este repositório apresenta uma solução robusta para automação da geração e entrega mensal de relatórios detalhados sobre a indisponibilidade de lojas nos últimos 30 dias. Desenvolvida em Python, a solução utiliza bibliotecas como mysql-connector para integração com MySQL, smtplib para envio de emails e datetime para manipulação de datas, permitindo a extração precisa de dados através de consultas SQL customizadas ao banco de dados configurado.

A solução identifica períodos de inatividade de lojas específicas e formata os resultados em um arquivo CSV estruturado. Ao final de cada mês, o relatório é automaticamente enviado por email, possibilitando que empresas de monitoramento forneçam aos clientes informações detalhadas sobre as lojas afetadas e a duração das indisponibilidades.

Funcionalidades principais:

Extração de dados via consultas SQL customizadas.
Geração automática de arquivo CSV com informações detalhadas.
Envio automatizado de relatórios por email.
Integração contínua com GitHub para execução programada.
Utilização de pipeline para garantir execução confiável e eficiente do processo.
Integração com GitHub e CI/CD:
O repositório utiliza GitHub Actions para implementar um pipeline de CI/CD, garantindo a execução automatizada, escalável e controlada do processo mensal de geração e envio de relatórios. Esta abordagem assegura uma operação contínua e confiável do back-end, facilitando o monitoramento e a análise de dados críticos de indisponibilidade.

Integração com Power BI:
O arquivo CSV gerado é facilmente integrado e analisado no Power BI, proporcionando insights adicionais através de visualizações detalhadas sobre as indisponibilidades das lojas monitoradas.
