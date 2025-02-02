from colorama import Fore,Style,Back
import os
import platform
import sys

# Adicionar o caminho absoluto da pasta libs ao sys.path.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../libs')))
# Dependendo de onde se importar o arquivo Basics pode ser nescessario adicionar "../".

# " from Basics import * " IMPORTA ALGUMAS COISAS PRESENTES EM TODOS OS PROGRAMAS PARA ECONOMIZAR LINHAS DE CODIGO.
# QUALQUER EDIÇÃO FEITA AQUI IRA AFETAR TODOS OS PROGRAMAS QUE IMPORTAM ESSE ARQUIVO.

# CORES BASICAS NORMALMENTE USADAS.
VERMELHO = Fore.RED    # GERALMENTE USADA EM ERROS.
VERDE = Fore.GREEN  # USADAS EM ALGO IMPORTANTE OU UM ERRO NÂO DESCOBERTO.
AZUL = Fore.BLUE    # GERALMENTE USADA EM MENSAGENS SOBRE RECARREGAR O PROGRMA APOS ERRO .
AMARELO = Fore.YELLOW   # USADA EM TRANCIÇÕE.S DE TELA, MENSAGENS DE AVISO/IMPORTANTES OU ENTRADA DO USUARIO.
CIANO = Fore.CYAN   # RESPOTA DO PROGRAMA AO USUARIO.
MAGENTA = Fore.MAGENTA  # SEM USOS.
BRANCO = Fore.WHITE   # USADA EM MENSAGENS DE INFORMAÇÃO.
PADRAO = Style.RESET_ALL    # COR PADRAO DO TERMINAL.

# LIMPAR TERMINAL DO USUARIO.
def limpar_terminal():
    if platform.system () == 'Windows':
        os.system('cls')
    else:
        os.system('clear')