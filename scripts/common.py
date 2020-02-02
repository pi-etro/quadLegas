# common.py
# metodos usados diversas vezes ou em todo o programa

from os.path import exists
from colorama import Fore
from os import name, remove, system
from scripts.data import endereco

# limpa o terminal
def clear():
    system('cls' if name == 'nt' else 'clear')
    return

# texto para metodos nao implementados
def fazer():
    print('Nao disponivel!')
    return

# limpa arquivos temporarios para sair do programa
def clean_exit():
    if exists(endereco('data/.fKfIASBfFufCPItc')):
        remove(endereco('data/.fKfIASBfFufCPItc'))
    return

# logo do programa
def logo():
    clear()
    print(  Fore.BLUE + '   _.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._._\n' +
            ' ,\'_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._._`.\n' +
            '( (                                                                               ) )\n' +
            ' ) ) ' +Fore.MAGENTA+ ' ██████' +Fore.CYAN+ '╗' +Fore.MAGENTA+ ' ██' +Fore.CYAN+ '╗' +Fore.MAGENTA+ '   ██' +Fore.CYAN+ '╗' +Fore.MAGENTA+ ' █████' +Fore.CYAN+ '╗ ' +Fore.MAGENTA+ '██████' +Fore.CYAN+ '╗ ' +Fore.MAGENTA+ '██' +Fore.CYAN+ '╗     ' +Fore.MAGENTA+ '███████' +Fore.CYAN+ '╗ ' +Fore.MAGENTA+ '██████' +Fore.CYAN+ '╗  ' +Fore.MAGENTA+ '█████' +Fore.CYAN+ '╗ ' +Fore.MAGENTA+ '███████' +Fore.CYAN+ '╗ ' +Fore.BLUE+ '( ( \n' +
            '( (  ' +Fore.MAGENTA+ '██' +Fore.CYAN+ '╔═══' +Fore.MAGENTA+ '██' +Fore.CYAN+ '╗' +Fore.MAGENTA+ '██' +Fore.CYAN+ '║   ' +Fore.MAGENTA+ '██' +Fore.CYAN+ '║' +Fore.MAGENTA+ '██' +Fore.CYAN+ '╔══' +Fore.MAGENTA+ '██' +Fore.CYAN+ '╗' +Fore.MAGENTA+ '██' +Fore.CYAN+ '╔══' +Fore.MAGENTA+ '██' +Fore.CYAN+ '╗' +Fore.MAGENTA+ '██' +Fore.CYAN+ '║     ' +Fore.MAGENTA+ '██' +Fore.CYAN+ '╔════╝' +Fore.MAGENTA+ '██' +Fore.CYAN+ '╔════╝ ' +Fore.MAGENTA+ '██' +Fore.CYAN+ '╔══' +Fore.MAGENTA+ '██' +Fore.CYAN+ '╗' +Fore.MAGENTA+ '██' +Fore.CYAN+ '╔════╝  ' +Fore.BLUE+ ') )\n' +
            ' ) ) ' +Fore.MAGENTA+ '██' +Fore.CYAN+ '║  ' +Fore.MAGENTA+ ' ██' +Fore.CYAN+ '║' +Fore.MAGENTA+ '██' +Fore.CYAN+ '║   ' +Fore.MAGENTA+ '██' +Fore.CYAN+ '║' +Fore.MAGENTA+ '███████' +Fore.CYAN+ '║' +Fore.MAGENTA+ '██' +Fore.CYAN+ '║  ' +Fore.MAGENTA+ '██' +Fore.CYAN+ '║' +Fore.MAGENTA+ '██' +Fore.CYAN+ '║     ' +Fore.MAGENTA+ '█████' +Fore.CYAN+ '╗  ' +Fore.MAGENTA+ '██' +Fore.CYAN+ '║  ' +Fore.MAGENTA+ '███' +Fore.CYAN+ '╗' +Fore.MAGENTA+ '███████' +Fore.CYAN+ '║' +Fore.MAGENTA+ '███████' +Fore.CYAN+ '╗ ' +Fore.BLUE+ '( ( \n' +
            '( (  ' +Fore.MAGENTA+ '██' +Fore.CYAN+ '║' +Fore.MAGENTA+ '▄▄ ██' +Fore.CYAN+ '║' +Fore.MAGENTA+ '██' +Fore.CYAN+ '║   ' +Fore.MAGENTA+ '██' +Fore.CYAN+ '║' +Fore.MAGENTA+ '██' +Fore.CYAN+ '╔══' +Fore.MAGENTA+ '██' +Fore.CYAN+ '║' +Fore.MAGENTA+ '██' +Fore.CYAN+ '║  ' +Fore.MAGENTA+ '██' +Fore.CYAN+ '║' +Fore.MAGENTA+ '██' +Fore.CYAN+ '║     ' +Fore.MAGENTA+ '██' +Fore.CYAN+ '╔══╝  ' +Fore.MAGENTA+ '██' +Fore.CYAN+ '║   ' +Fore.MAGENTA+ '██' +Fore.CYAN+ '║' +Fore.MAGENTA+ '██' +Fore.CYAN+ '╔══' +Fore.MAGENTA+ '██' +Fore.CYAN+ '║╚════' +Fore.MAGENTA+ '██' +Fore.CYAN+ '║  ' +Fore.BLUE+ ') )\n' +
            ' ) ) ' +Fore.CYAN+ '╚' +Fore.MAGENTA+ '██████' +Fore.CYAN+ '╔╝╚' +Fore.MAGENTA+ '██████' +Fore.CYAN+ '╔╝' +Fore.MAGENTA+ '██' +Fore.CYAN+ '║  ' +Fore.MAGENTA+ '██' +Fore.CYAN+ '║' +Fore.MAGENTA+ '██████' +Fore.CYAN+ '╔╝' +Fore.MAGENTA+ '███████' +Fore.CYAN+ '╗' +Fore.MAGENTA+ '███████' +Fore.CYAN+ '╗╚' +Fore.MAGENTA+ '██████' +Fore.CYAN+ '╔╝' +Fore.MAGENTA+ '██' +Fore.CYAN+ '║  ' +Fore.MAGENTA+ '██' +Fore.CYAN+ '║' +Fore.MAGENTA+ '███████' +Fore.CYAN+ '║ ' +Fore.BLUE+ '( ( \n' +
            '( (  ' +Fore.MAGENTA+ ' ' +Fore.CYAN+ '╚══' +Fore.MAGENTA+ '▀▀' +Fore.CYAN+ '═╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝  ' +Fore.BLUE+ ') )\n' +
            ' ) )                                                                     ' +Fore.GREEN+ 'pi-etro' +Fore.BLUE+ ' ( ( \n' +
            '( (_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-) )\n' +
            ' `._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.,\'' +Fore.RESET)
    return

# welcome e menu central
def welcome():
    print(  '                               Bem vindo ao quadLegas!\n' +
            '                  Uma ferramenta para explorar a matricula da UFABC\n')

    print(  '1 Descobrir colegas de turma por RA\n' +
            '2 Descobrir colegas de turma com os codigos das turmas\n' +
            '3 Importar pdf de matriculas deferidas\n' +
            '4 Sair\n')
    return

# conjunto de logo mais welcome
def lw():
    logo()
    welcome()
    return
