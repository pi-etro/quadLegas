# menus.py
# implementa os menus e entradas do usuario

from scripts.common import clean_exit, clear, logo, lw
from scripts.colCod import colCod
from scripts.colRa import colRa
from scripts.data import importDef, load_dfs, endereco
from pandas import DataFrame
from os import path

# welcome e menu principal do programa
def central():
    lw()

    df_deferidas = DataFrame()
    df_changed = False
    df_nomeras = DataFrame()

    sel = 0
    while sel!='4':
        print(':',end='')
        sel = input()

        if sel=='1':
            if path.exists(endereco('data/csv/deferidas.csv')) and path.getsize(endereco('data/csv/deferidas.csv')) > 1:
                df_deferidas, df_changed, df_nomeras = load_dfs(df_deferidas, df_changed, df_nomeras)
                menu_colRa(df_deferidas, df_nomeras)
            else:
                print('Importe o pdf de matriculas!')
        elif sel=='2':
            if path.exists(endereco('data/csv/deferidas.csv')) and path.getsize(endereco('data/csv/deferidas.csv')) > 1:
                df_deferidas, df_changed, df_nomeras = load_dfs(df_deferidas, df_changed, df_nomeras)
                menu_colCod(df_deferidas, df_nomeras)
            else:
                print('Importe o pdf de matriculas!')
        elif sel=='3':
            df_changed = menu_importar()
        else:
            print('Opcao invalida!')

    clear()
    clean_exit()
    return

# menu para importar pdf de matriculas
def menu_importar():
    logo()

    print(  '                         Importar pdf de matriculas deferidas\n')
    print(  '0 Voltar ao menu\n')

    print(  'Entre com o endereco do pdf de matriculas deferidas')

    invalid = True
    while invalid:
        print(':',end='')
        ad = input()
        if ad=='0':
            lw()
            return
        if path.exists(ad):
            if path.isfile(ad):
                if ad[-4:].lower() == '.pdf':
                    invalid = False
                else:
                    print('Arquivo nao eh um .pdf!')
            else:
                print('Endereco nao eh de um arquivo!')
        else:
            print('Endereco invalido!')

    print('Importando...')
    importDef(ad)
    print('Importacao conluida')

    input('Aperte ENTER para voltar ao menu')
    lw()
    return True

# menu para listar colegas de uma lista de codigos
def menu_colCod(df_deferidas, df_nomeras):
    logo()

    print(  '                 Descobrir colegas de turma com os codigos das turmas\n')
    print(  '0 Voltar ao menu\n')

    print(  'Quantas turmas deseja consultar?')

    invalid = True
    while invalid:
        print(':',end='')
        n=input()
        if n=='0':
            lw()
            return
        if (n.isdigit()):
            invalid = False
        else:
            print('Entrada invalida!')

    c=0
    lista_cod = []
    while c!=int(n):
        print(  'Entre com o codigo da %d turma' % (c+1))
        print(':',end='')
        x = input()
        if x=='0':
            lw()
            return
        lista_cod.append(x)
        c += 1

    print(  'Entre com local para salvar a planilha')

    invalid = True
    while invalid:
        print(':',end='')
        ad=input()
        if ad=='0':
            lw()
            return
        if path.exists(path.dirname(ad)):
            if path.exists(ad):
                if path.isfile(ad):
                    if ad[-4:].lower() == '.csv':
                        print('Sobrescrever arquivo existente?(s/n)')
                        print(':',end='')
                        x=input()
                        if ad=='0':
                            lw()
                            return
                        if x.lower()=='s':
                            invalid = False
                        else:
                            print('Entre com outro local para salvar a planilha')
                    else:
                        print('Arquivo nao eh um .csv!')
                else:
                    print('Endereco nao eh de um arquivo!')
            else:
                if ad[-4:].lower() == '.csv':
                    invalid = False
                else:
                    print('Arquivo nao eh um .csv!')
        else:
            print('Endereco invalido!')

    print('Gerando planilha...')
    colCod(df_deferidas, df_nomeras, lista_cod, ad)
    print('Planilha salva em: '+ad)

    input('Aperte ENTER para voltar ao menu')
    lw()
    return

# menu para listar colegas nas mesmas turmas de ra
def menu_colRa(df_deferidas, df_nomeras):
    logo()

    print(  '                          Descobrir colegas de turma por RA\n')
    print(  '0 Voltar ao menu\n')

    print(  'Entre com seu RA')

    invalid = True
    while invalid:
        print(':',end='')
        ra=input()
        if ra=='0':
            lw()
            return
        if (ra.isdigit()):
            invalid = False
        else:
            print('RA invalido!')

    print(  'Entre com local para salvar a planilha')

    invalid = True
    while invalid:
        print(':',end='')
        ad=input()
        if ad=='0':
            lw()
            return
        if path.exists(path.dirname(ad)):
            if path.exists(ad):
                if path.isfile(ad):
                    if ad[-4:].lower() == '.csv':
                        print('Sobrescrever arquivo existente?(s/n)')
                        print(':',end='')
                        x=input()
                        if ad=='0':
                            lw()
                            return
                        if x.lower()=='s':
                            invalid = False
                        else:
                            print('Entre com outro local para salvar a planilha')
                    else:
                        print('Arquivo nao eh um .csv!')
                else:
                    print('Endereco nao eh de um arquivo!')
            else:
                if ad[-4:].lower() == '.csv':
                    invalid = False
                else:
                    print('Arquivo nao eh um .csv!')
        else:
            print('Endereco invalido!')

    print('Gerando planilha...')
    colRa(df_deferidas, df_nomeras, ra, ad)
    print('Planilha salva em: '+ad)

    input('Aperte ENTER para voltar ao menu')
    lw()
    return
