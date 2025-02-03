import subprocess
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../libs')))
from Basics import *
while True:
    limpar_terminal()
    print(AMARELO + "-+-Digite (voltar) para voltar-+-")
    time.sleep(0.5)
    print(PADRAO+"Oque deseja descobrir?")
    print(CIANO + """
-Progressão Geometrica (PG)
-Progressão Aritimetica (PA) """)
    i = str(input(PADRAO + "")).strip().lower()
    limpar_terminal()
    if i == 'voltar':
        limpar_terminal()
        print(AMARELO + "\nVoltando...\n")
        time.sleep(1)
        limpar_terminal()
        subprocess.run(['python', 'mcf_hub.py'])
    elif i == 'pa':
        limpar_terminal()
        print(VERDE + "Carregando P.A aguarde...")
        time.sleep(2.0)
        limpar_terminal()
        subprocess.run(['python', 'math_utils/pga/pa.py'])
        break
    elif i == 'pg':
        limpar_terminal()
        print(VERDE + "Carregando P.G aguarde...")
        time.sleep(2.0)
        limpar_terminal()
        subprocess.run(['python', 'math_utils/pga/pg.py'])
        break
    else:
        print("Erro:Função inexistente tente novamente.")
        limpar_terminal()
        print(VERMELHO + "Erro:Função inexistente.")
        time.sleep(2.5)
        print(AZUL + "Recarregando o programa...")
        time.sleep(1)
        limpar_terminal()