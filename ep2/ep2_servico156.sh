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
COMPLETE_ARQ="arquivocompleto.csv"
SELECTED_FILE="$COMPLETE_ARQ" # começa com o arquivo completo, caso nenhum tenha sido selecionado
FILTERS=()
FILTERED_FILE="filtered_data.csv"
AUX_FILE="$SELECTED_FILE"
files=()

# funções obrigatórias
selecionar_arquivo() {
    echo " "
    echo "Escolha uma opção de arquivo."

    # irá mostrar todas opções para seleção 
    select arq in $files; do
        if [[ -n "$arq" ]]; then
            # guardamos o arquivo selecionado e limpamos os filtros
            SELECTED_FILE="$arq"
            # auxiliar para guardarmos o arquivo original e podermos "remover" os filtros
            AUX_FILE="$SELECTED_FILE" 
            FILTERS=()
            echo "+++ Arquivo atual: $SELECTED_FILE"
            numero_reclamacoes
            break
        fi
    done    
}

adicionar_filtro_coluna() {

    # pega a primeira linha do arquivo, que contém as colunas
    columns=$(head -n 1 "$SELECTED_FILE")
    # converte a linha em vários "itens", ou seja, separa o nome das colunas
    IFS=';' read -ra col <<< "$columns" 

    echo " "
    echo "Escolha uma opção de coluna para o filtro:"

    select c in "${col[@]}"; do
        if [[ -n "$c" ]]; then

            uniq_values=$(tail -n +2 "$SELECTED_FILE" | cut -d';' -f"$REPLY" | sort | uniq)

            echo " "
            echo "Escolha uma opção de valor para $c:"
            IFS=$'\n'
            select val in $uniq_values; do
                if [[ -n "$val" ]]; then
                    echo "+++ Adicionado filtro: $c = $val"
                    FILTERS+=("$c,$val") # guarda a coluna e o valor para poder printar todos filtros

                    head -n 1 "$SELECTED_FILE" > temp_file
                    grep "$val" "$SELECTED_FILE" >> temp_file
                    mv temp_file "$FILTERED_FILE"
                
                    SELECTED_FILE="$FILTERED_FILE"

                    imprime_filtros
                    break
                fi
            done
            break
        fi
    done
}

limpar_filtros_colunas() {
    FILTERS=()
    SELECTED_FILE="$AUX_FILE" # volta a ser o arquivo original, que guardamos

    echo +++ Filtros removidos
    echo "+++ Arquivo atual: $SELECTED_FILE"
    numero_reclamacoes
}

mostrar_duracao_media_reclamacao() {
    # data de abertura -  1 coluna
    # data do parecer - 13 coluna

    sum_sec=0
    count=0

    while IFS=';' read -r linha; do
        da=$(echo "$linha" | cut -d';' -f 1) # data de abertura
        dp=$(echo "$linha" | cut -d';' -f 13) # data de parecer

        diff_sec=$(bc <<< "$(date -d "$dp" +%s) - $(date -d "$da" +%s)")
        sum_sec=$((sum_sec + diff_sec))
        count=$((count + 1))

    done < <(tail -n +2 "$SELECTED_FILE")

    days=$(bc <<< "$sum_sec / 86400") # um dia tem 86400 segundos
    aver=$(bc <<< "$days / $count")

    echo +++ Duração média da reclamação: $aver dias
    echo +++++++++++++++++++++++++++++++++++++++
}

mostrar_ranking_reclamacoes() {
    
    columns=$(head -n 1 "$SELECTED_FILE")
    IFS=';' read -ra col <<< "$columns"  

    echo " "
    echo "Escolha uma opção de coluna para o análise:"

    select c in "${col[@]}"; do
        if [[ -n "$c" ]]; then

            ranking=$(tail -n +2 "$SELECTED_FILE" | cut -d';' -f"$REPLY" | sort | uniq -c | sort -n -r | head -n 5)
            echo +++ "$c" com mais reclamações:
            echo "$ranking"
            echo +++++++++++++++++++++++++++++++++++++++
            break
        fi
    done
}           

mostrar_reclamacoes() {
    (tail -n +2 "$SELECTED_FILE" | cat)
    imprime_filtros
}


# funções auxiliares
imprime_filtros() {

    echo "+++ Arquivo atual: $AUX_FILE"
    echo "+++ Filtros atuais:"


    IFS=',' read -r name value <<< "${FILTERS[0]}"
    output="$name = $value"
    for ((i = 1; i < ${#FILTERS[@]}; i++)); do
        IFS=',' read -r name value <<< "${FILTERS[i]}"
        output+=" | $name = $value"
    done

    echo "$output"
    numero_reclamacoes
}

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
    head -n 1 "$(ls "$DATA_DIR"/*.csv | head -n 1)" > "$COMPLETE_ARQ"
    
    # coloca todas as linhas de todos arquivos, exceto a primeira (nome das colunas)
    for arq in "$DATA_DIR"/*.csv; do
        tail -n +2 "$arq" >> "$COMPLETE_ARQ"
    done
}

operacoes() {
    while true; do
        echo " "
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
        cd $DATA_DIR
        # guarda todos arquivos que existem no nosso diretorio
        files=$(ls *.csv 2>/dev/null)
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
        cd $DATA_DIR
        # guarda todos arquivos que existem no nosso diretorio
        files=$(ls *.csv 2>/dev/null)
        operacoes
    fi
fi