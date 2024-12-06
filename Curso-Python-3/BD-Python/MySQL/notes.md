
# Este script contém vários comandos Docker e PowerShell para gerenciar contêineres Docker e arquivos.

Comandos:
1. `docker-compose up -d`: Inicia os contêineres Docker definidos no arquivo `docker-compose.yml` em modo desacoplado.
2. `docker-compose down`: Para e remove os contêineres Docker definidos no arquivo `docker-compose.yml`.
3. `docker start [id do contêiner]`: Inicia um contêiner Docker específico usando seu ID de contêiner.
4. `docker stop [id do contêiner]`: Para um contêiner Docker específico usando seu ID de contêiner.
5. `docker ps`: Lista todos os contêineres Docker em execução.
6. `Remove-Item -Recurse -Force .\mysql_206`: Remove recursivamente e forçadamente o diretório `mysql_206` e seu conteúdo usando PowerShell.
7. `docker exec -it [id do contêiner] /bin/bash`: Abre um terminal interativo dentro de um contêiner Docker em execução.
8. `docker logs [id do contêiner]`: Exibe os logs de um contêiner Docker específico.
9. `docker rm [id do contêiner]`: Remove um contêiner Docker específico usando seu ID de contêiner.
10. `docker rmi [id da imagem]`: Remove uma imagem Docker específica usando seu ID de imagem.
11. `docker-compose build`: Constrói ou reconstrói os serviços definidos no arquivo `docker-compose.yml`.
12. `Get-Process`: Lista todos os processos em execução no sistema usando PowerShell.
13. `Stop-Process -Name [nome do processo]`: Para um processo específico pelo nome usando PowerShell.
14. `Get-ChildItem -Recurse`: Lista todos os arquivos e diretórios recursivamente a partir do diretório atual usando PowerShell.

