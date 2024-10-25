#!/bin/bash

# Cabeçalho do arquivo
##################################################################
# MAC0216 - Técnicas de Programação I (2024)
# EP2 - Programação em Bash
#
# Nome do(a) aluno(a) : Thainara de Assis Goulart
# NUSP : 13874413
##################################################################

DATA_DIR="data"
COMPLETE_ARQ="$DATA_DIR/arquivocompleto.csv"
SELECTED_FILE="$COMPLETE_ARQ" # começa com o arquivo completo, caso nenhum tenha sido selecionado

# funções obrigatórias
selecionar_arquivo() {
    echo "Escolha uma opção de arquivo."

    # guarda todos arquivos que existem no nosso diretorio
    arquivos=$(ls $DATA_DIR/*.csv 2>/dev/null)

    # irá mostrar todas opções para seleção 
    select arq in $arquivos; do
        if [[ -n "$arq" ]]; then
            # guardamos o arquivo selecionado
            SELECTED_FILE="$arq"
            echo "+++ Arquivo atual: $SELECTED_FILE"
            numero_reclamacoes
            break
        fi
    done    
}

# adicionar_filtro_coluna() {

# }

# limpar_filtros_colunas() {

# }

# mostrar_duracao_media_reclamacao() {

# }

# mostrar_ranking_reclamacoes() {

# }
# mostrar_reclamacoes() {

# }


# funções auxiliares
numero_reclamacoes() {
    # conta todas as linhas do arquivo, exceto a primeira
    num_recl=$(tail -n +2 "$SELECTED_FILE" | wc -l)
    echo "+++ Número de reclamações: $num_recl"
    echo "+++++++++++++++++++++++++++++++++++++++"
}

baixar_arq_url() {
    urls_file=$1

    # criando o diretório que armazenará nossos dados, ou seja, os aquivos .csv
    mkdir -p "$DATA_DIR"
    wget -nv -i "$urls_file" -P "$DATA_DIR"
}

converter_codificacoes() {
    for arq in "$DATA_DIR"/*.csv; do
        # converte o arquivo e salva em <nome_do_arquivo_utf8.csv>
        iconv -f ISO-8859-1 -t UTF-8 "$arq" -o "${arq%.csv}_utf8.csv" 
        # iremos transformar para o nome original novamente <nome_do_arquivo.csv>
        mv "${arq%.csv}_utf8.csv" "$arq"
    done
}

junta_arquivos() {

    # coloca o cabeçalho do primeiro arquivo csv no arquivo completo
    head -n 1 "$DATA_DIR"/*.csv | head -n 1 > "$COMPLETE_ARQ"
    
    # coloca todas as linhas de todos arquivos, exceto a primeira (nome das colunas)
    for arq in "$DATA_DIR"/*.csv; do
        tail -n +2 "$arq" >> "$COMPLETE_ARQ"
    done
}

operacoes() {
    while true; do
        echo "Escolha uma opção de operação:"
        echo "1) selecionar_arquivo"
        echo "2) adicionar_filtro_coluna"
        echo "3) limpar_filtros_colunas"
        echo "4) mostrar_duracao_media_reclamacao"
        echo "5) mostrar_ranking_reclamacoes"
        echo "6) mostrar_reclamacoes"
        echo "7) sair"
        read -p "#? " opcao

        case $opcao in
            1) selecionar_arquivo ;;
            2) adicionar_filtro_coluna ;;
            3) limpar_filtros_colunas ;;
            4) mostrar_duracao_media_reclamacao ;;
            5) mostrar_ranking_reclamacoes ;;
            6) mostrar_reclamacoes ;;
            7) echo "Fim do programa" ; echo "+++++++++++++++++++++++++++++++++++++++" ; exit 0 ;;
            *) echo "Opção inválida" ;;
        esac
    done
}


#########################################################################
# execução "principal" do programa
echo "+++++++++++++++++++++++++++++++++++++++"
echo "Este programa mostra estatísticas do"
echo "Serviço 156 da Prefeitura de São Paulo"
echo "+++++++++++++++++++++++++++++++++++++++"

if [[ $# -eq 1 ]]; then

    # primeiro verifica se o arquivo existe
    if [[ ! -f "$1" ]]; then
        echo "ERRO: O arquivo "$1" não existe."
        exit 1
    else
        baixar_arq_url "$1"
        converter_codificacoes
        junta_arquivos
        operacoes
    fi

else
    # para chamada sem parâmetro, verifica se o diretório de dados existe
    # se não existe, imprimira a mensagem de erro
    if [[ ! -d "$DATA_DIR" ]]; then
        echo "ERRO: Não há dados baixados."
        echo "Para baixar os dados antes de gerar as estatísticas, use:"
        echo "  ./ep2_servico156.sh <nome do arquivo com URLs de dados do Serviço 156>"    
        exit 1
    # se existe, irá executar as opçoes normalmente     
    else
        operacoes
    fi
fi