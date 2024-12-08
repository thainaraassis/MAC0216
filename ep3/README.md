# EP3 - TEXTRIS

## AUTOR(ES): com nome, NUSP e endereço de e-mail

- Júlia Calixto Rosa, 13749490, juliacalixtorosa@usp.br
- Thainara Assis

## DESCRIÇÃO:

Textris é uma versão simplificada do clássico jogo de Tetris, desenvolvida para ser jogada no terminal. O jogo exibe um tabuleiro de Tetris em formato de matriz no terminal, e o jogador pode controlar as peças utilizando as teclas do teclado.

## COMO EXECUTAR:

Explicando como o programa deve ser executado, os eventuais argumentos de linha de comando do programa (o que é o argumento, como ele precisa estar formatado, etc.). Fale também sobre como a documentação é gerada.

- Utilizamos um ambiente virtual para executar o programa. Para isso, siga os passos abaixo:

    1. Criar um Ambiente Virtual:

        ```bash
        python3.12 -m venv venv
        ```

    2. Ativar o Ambiente Virtual:

        ```bash
        source venv/bin/activate
        ```

    3. Instalar os Pacotes Necessários:

        ```bash
        pip install readchar
        ```

    4. Executar o Programa:

        ```bash
        python src/main.py
        ```

    5. Para desativar o Ambiente Virtual:

        ```bash
        deactivate
        ```

- Para gerar a documentação, siga as instruções pertinentes para o seu projeto.

## TESTES:

Foram realizados testes unitários utilizando a ferramenta pytest para garantir o funcionamento correto das principais funcionalidades do sistema. Os testes estão localizados na pasta `test/`, e cada arquivo de teste corresponde a um conjunto de verificações para os principais métodos e componentes que são essenciais para o funcionamento do jogo.

## DEPENDÊNCIAS:

- Sistema Operacional: Ubuntu 24.04 LTS
- Python: 3.12.3
- Pacotes:

    ```bash
    pip install readchar
    ```
    ```bash
    pip install pytest
    ```

