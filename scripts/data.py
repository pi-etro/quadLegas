# data.py
# codigos para carregar dados

from os.path import exists, abspath, join
from os import remove
from pandas import read_csv
from scripts.cry import decra
import sys

# carrega os df com os csv
def load_dfs(df_deferidas, df_nomeras,quad):

    # carragar df de matriculas
    df_deferidas = read_csv(endereco(quad))

    # carregar df de nomes e ras
    if not exists(endereco('data/.fKfIASBfFufCPItc')):
            decra()
    df_nomeras = read_csv(endereco('data/.fKfIASBfFufCPItc'), encoding = 'Latin-1')

    if exists(endereco('data/.fKfIASBfFufCPItc')):
        remove(endereco('data/.fKfIASBfFufCPItc'))

    #retorna os dfs atualizados e o estado do df de matriculas
    return df_deferidas, df_nomeras

def endereco(relativo):
    try:
        end = sys._MEIPASS
    except Exception:
        end = abspath('.')
    return join(end, relativo)
