# menus.py
# implementa os menus e entradas do usuario

from scripts.common import clear, logo, lw
from scripts.colCod import colCod
from scripts.colRa import colRa
from scripts.data import load_dfs, endereco
from pandas import DataFrame
from os import path

nquad1='2019.3'
nquad2='2020.1'
nquad3=''

quad1='data/csv/2019.3.csv'
quad2='data/csv/2020.1.csv'
quad3=''

# welcome e menu principal do programa
def central():
    lw()

    sel = 0
    while sel!='4':
        print(':',end='')
        sel = input()

        if sel=='1':
            menu_colRa()
        elif sel=='2':
            menu_colCod()
        else:
            print('Opcao invalida!')
    clear()
    return

# menu para listar colegas de uma lista de codigos
def menu_colCod():
    logo()

    print(  '                 Descobrir colegas de turma com os codigos das turmas\n')
    print(  '[1] ' + nquad1)
    print(  '[2] ' + nquad2)
    print(  '[0] Voltar ao menu\n')
    
    invalid = True
    while invalid:
        print(':',end='')
        n=input()
        if n=='0':
            lw()
            return
        if n=='1':
            quad = quad1
        if n=='2':
            quad = quad2
        if (n.isdigit()):
            invalid = False
        else:
            print('Entrada invalida!')
    
    df_deferidas = DataFrame()
    df_nomeras = DataFrame()
    
    df_deferidas, df_nomeras = load_dfs(df_deferidas, df_nomeras, quad)
    
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
        print(  'Entre com o codigo da turma %d' % (c+1))
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

    input('\nAperte ENTER para voltar ao menu')
    lw()
    return

# menu para listar colegas nas mesmas turmas de ra
def menu_colRa():
    logo()

    print(  '                          Descobrir colegas de turma por RA\n')
    print(  '[1] ' + nquad1)
    print(  '[2] ' + nquad2)
    print(  '[0] Voltar ao menu\n')
    
    invalid = True
    while invalid:
        print(':',end='')
        n=input()
        if n=='0':
            lw()
            return
        if n=='1':
            quad = quad1
        if n=='2':
            quad = quad2
        if (n.isdigit()):
            invalid = False
        else:
            print('Entrada invalida!')
    
    df_deferidas = DataFrame()
    df_nomeras = DataFrame()
    
    df_deferidas, df_nomeras = load_dfs(df_deferidas, df_nomeras, quad)

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

    input('\nAperte ENTER para voltar ao menu')
    lw()
    return
