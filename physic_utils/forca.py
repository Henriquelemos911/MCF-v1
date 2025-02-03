import subprocess
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../libs')))
from Basics import *

while True:
    print(AMARELO + "-+-Digite (voltar) para voltar-+-\n")
    print(PADRAO + "Vamos Calcular Força!\n")
    time.sleep(0.5)
    valores = input()("Qual a massa e aceleraçao do objeto?\n(escreva respectivamente dividido por espaço)").lower()
    
    if valores == 'voltar':
        print(AMARELO + "\nVoltando...\n")
        time.sleep(2.5)
        limpar_terminal()
        subprocess.run(['python', 'mcf_hub.py'])
        break 
    try:
        m, a = map(float, valores.split())
        f = m*a
        print('calculando valor da força desse objeto...\n')
        time.sleep(0.5)
        print(f"-A Força deste objeto e de ",f,"N")
        print("\n\n\n")
        time.sleep(3)
    except ValueError:
        limpar_terminal()
        print(VERMELHO + "Erro:Digite numeros válidos (letras não são suportadas).")
        time.sleep(2.5)
        print(AZUL + "Recarregando o programa...")
        time.sleep(1)
        limpar_terminal()