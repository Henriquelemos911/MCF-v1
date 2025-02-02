import subprocess
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../libs')))
from Basics import *
while True:
    print(AMARELO+"-+-Digite (voltar) para voltar-+-\n")
    try:
        print(PADRAO+"Oque deseja descobrir?")
        print(CIANO+"""
-O valor da hipotenusa (H)
-O valor do cateto(C)""")
        i = input(AMARELO+"").lower()
        
        if i == 'voltar':
            limpar_terminal()
            print(AMARELO + "\nVoltando...\n")
            time.sleep(2.5)
            limpar_terminal()
            subprocess.run(['python', 'mcf_hub.py'])
            break  
        elif i == 'h':
            print(AMARELO+"Carregando calculo de hipotenusa.")
            time.sleep(2)
            limpar_terminal()
            subprocess.run(['python', 'math_utils/pit/pit_hipo.py'])
            break
        elif i == 'c':
            print(AMARELO+"Carregando calculo de cateto.")
            time.sleep(2.5)
            limpar_terminal()
            subprocess.run(['python', 'math_utils/pit/pit_cat.py'])
            break
        else:
            limpar_terminal()
            print(VERMELHO+"Erro:Função inexistente tente novamente.")
            time.sleep(1)
            print(AZUL+"Recarregando o programa...")
            time.sleep(2.5)
            limpar_terminal()
    except ValueError:
        print(VERMELHO+"\nErro:Ops algo deu errado tente novamente!\n")
        time.sleep(1)
        print(AZUL+"Recarregando o programa...")
        time.sleep(2.5)
        limpar_terminal