# data.py
# codigos para carregar dados

from tabula import convert_into
from os.path import exists, abspath, join
from os import remove, rename
from pandas import read_csv
from scripts.cry import decra
import sys

# metodo que importa matriculas do pdf e salva em um csv
def importDef(deferidas):

    # deletar o arquivo se existir
    if exists(endereco('data/csv/deferidas.csv')):
        remove(endereco('data/csv/deferidas.csv'))

    # converter para csv e salvar na pasta interna do programa
    convert_into(deferidas,endereco('data/csv/deferidas.csv'), output_format='csv', pages='all')

    # remover header repetido, copiando o arquivo csv para um novo e substituindo o antigo
    with open(endereco('data/csv/deferidas.csv'), 'r') as old, open(endereco('data/csv/temp_deferidas.csv'), 'w') as new:
        header = old.readline()
        new.write('ra,turma\n')
        for line in old:
            if(line!=header):
                splited = line.split(',')
                linha = splited[0]+','+splited[1]+'\n'
                new.write(linha)
    remove(endereco('data/csv/deferidas.csv'))
    rename(endereco('data/csv/temp_deferidas.csv'),endereco('data/csv/deferidas.csv'))
    return

# carrega os df com os csv
def load_dfs(df_deferidas, df_changed, df_nomeras):
    print('Carregando dados...')

    # se o df de matriculas for vazio ou tiver mudado, carregar
    if df_deferidas.empty or df_changed:
        df_deferidas = read_csv(endereco('data/csv/deferidas.csv'))
        df_changed = False
        print('Matriculas deferidas carregadas com sucesso')
    else:
        print('Matriculas ja carregadas')

    # se o df de nomes e ras estiver vazio, carregar
    if df_nomeras.empty:
        if not exists(endereco('data/.fKfIASBfFufCPItc')):
            decra()
        df_nomeras = read_csv(endereco('data/.fKfIASBfFufCPItc'), encoding = 'Latin-1')
        print('RAs carregados com sucesso')
    else:
        print('RAs ja carregados')

    print('Carregamento dos dados concluido')

    if exists(endereco('data/.fKfIASBfFufCPItc')):
        remove(endereco('data/.fKfIASBfFufCPItc'))

    #retorna os dfs atualizados e o estado do df de matriculas
    return df_deferidas, df_changed, df_nomeras

def endereco(relativo):
    try:
        end = sys._MEIPASS
    except Exception:
        end = abspath('.')
    return join(end, relativo)
