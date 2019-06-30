# JogoBaixoJobLoadData
Este projeto é um microserviço desenvolvido em Python para o projeto **Jogo baixo**. Será responsável por consultar as API externas para obter os dados da temporada da NBA e salvar estas informações em um banco de dados para ser consultado pela Web API do Jogo Baixo.

## Getting start
1. Acessar ambiente virtual (ver arquivo na task de como fazer isso);
2. Executar o comando para instalar as dependências do projeto:
    ``` sh
    pip install -r requirements.txt
    ```
3. Para executar o projeto, execute o comando
    ``` sh
    python run.py
    ```

## Outros comandos
- Executar testes automatizados:
    ``` sh
    pytest
    ```
- Coverage dos testes:
    ```
    coverage run -m pytest
    ```
- Relatório do coverage de testes:
    ```
    coverage report
    ```

## Links para estudos
- [Tutorial pytest](https://blog.cedrotech.com/pytest-faca-testes-e-gere-relatorios-rapidamente/)
- [Schedule jobs](https://github.com/dbader/schedule)
