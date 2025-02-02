#calcular hipotenusa
import time
import subprocess
import math
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../libs')))
from Basics import *

while True:
    print(AMARELO+"-+-Digite (voltar) para voltar-+-\n")
    print(PADRAO+"Vamos descobrir o valor do hipotenusa!\n")
    try:
        time.sleep(0.5)
        print("Qual o valor dos dois catetos? \n(separe com espaço): ")
        valores = input(AMARELO+"").lower()  
        if valores == 'voltar':
            print(AMARELO + "\nVoltando...\n")
            time.sleep(2.5)
            limpar_terminal()
            subprocess.run(['python', 'math_utils/pit/pit_hub.py'])
            break  

        c1, c2 = map(float, valores.split())
        h2 = c1**2 + c2**2
        hipo = math.sqrt(h2)
        print()
        print(f"O valor da hipotenusa é: {hipo}") 
        time.sleep(3)
        print("\n"*2)
        
    except ValueError:
        print(VERMELHO+"Erro: Por favor, insira dois números validos separados por espaço.")
        time.sleep(1)
        print(AZUL+"Recarregando o programa...")
        time.sleep(2.5)
        limpar_terminal()
        continue

    