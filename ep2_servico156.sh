#!/bin/bash

# Cabeçalho do arquivo
##################################################################
# MAC0216 - Técnicas de Programação I (2024)
# EP2 - Programação em Bash
#
# Nome do(a) aluno(a) : Thainara de Assis Goulart
# NUSP : 13874413
##################################################################


baixar_arq_url() {
    urls_file=$1

    # criando o diretório que armazenará nossos dados, ou seja, os aquivos .csv
    mkdir -p "$data"
    wget -nv -i "$urls_file" -P "$data"
}

if [[ $# -eq 1 ]]; then
    baixar_arq_url "$1"
else
    echo "ERRO: Não há dados baixados."
    echo "Para baixar os dados antes de gerar as estatísticas, use:"
    echo "  ./ep2_servico156.sh <nome do arquivo com URLs de dados do Serviço 156>"
                
    exit 1
fi