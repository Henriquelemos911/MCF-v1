import subprocess
import math
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../libs')))
from Basics import *

while True:                     
    print(AMARELO + "-+-Digite (voltar) para voltar-+-\n")
    print(PADRAO + "Vamos Calcular Raiz Quadrada!\n")
    time.sleep(0.5)
    num = input("- Digite o numero para descobrir sua raiz: ")
    if num.lower() == 'voltar':
        print(AMARELO + "\nVoltando...\n")
        time.sleep(2.5)
        limpar_terminal()
        subprocess.run(['python', 'mcf_hub.py'])
        break 
    try:
        num = float(num)
        raiz = math.sqrt(num)
        print('calculando sua raiz aguarde...\n')
        time.sleep(0.5)
        print(f'- A raiz quadrada de "{num}" e igual a:{raiz}\n\n')
    except ValueError:
        limpar_terminal()
        print(VERMELHO + "Erro:Digite um número válido (letras não são suportadas).")
        time.sleep(2.5)
        print(AZUL + "Recarregando o programa...")
        time.sleep(1)
        limpar_terminal()