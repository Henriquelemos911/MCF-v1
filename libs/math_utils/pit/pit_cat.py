import time
import subprocess
import math
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../libs')))
from Basics import *
#calcular cateto
while True:
    print(AMARELO+"-+-Digite (voltar) para voltar-+-\n")
    print(PADRAO+"Vamos descobrir o valor do cateto!\n")
    try:
        time.sleep(0.5)
        print("Qual o valor do cateto e da hipotenusa? \n(escreva respectivamente e separe com espaço): ")
        valores = input(AMARELO+"").lower()  
        if valores == 'voltar':
            print(AMARELO + "\nVoltando...\n")
            time.sleep(2.5)
            limpar_terminal()
            subprocess.run(['python', 'math_utils/pit/pit_hub.py'])
            break  
        
        c1, h = map(float, valores.split())
        
        if h > c1:  
            c22 = h**2 - c1**2
            cateto2 = math.sqrt(c22)
            print()
            print(CIANO+f"O valor do outro cateto é: ", cateto2)
            time.sleep(3)
        else:
            print(VERMELHO+"Erro: O valor da hipotenusa deve ser maior que o do cateto.\n")
            time.sleep(1)
            print(AZUL+"Recarregando o programa...")
            time.sleep(2.5)
            limpar_terminal()
    except ValueError:
        print(VERMELHO+"\nErro:digite numeros validos!\n")
        time.sleep(1)
        print(AZUL+"Recarregando o programa...")
        time.sleep(2.5)
        limpar_terminal()