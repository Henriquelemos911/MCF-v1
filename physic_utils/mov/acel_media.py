#acel media
# am= ∆v / ∆t
import time
import subprocess
import math
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../libs')))
from Basics import *
while True:
        print(AMARELO+"-+-Digite (voltar) para voltar-+-\n")
        print(PADRAO+"Vamos Calcular Aceleração Media!")
        time.sleep(0.5)
        valores = input("Qual a variação de velocidade (m/s) e o tempo de intervalo a se calcular?\n(escreva respectivamente dividido por espaço)").lower()
        
        if valores == 'voltar':
            limpar_terminal()
            print(AMARELO + "\nVoltando...\n")
            time.sleep(1)
            limpar_terminal()
            subprocess.run(['python', 'physic_utils/mov/mov_hub.py'])
            break
        try:
            v,t = map(float, valores.split())
            am = v / t
            print(AMARELO+'calculando aceleração media aguarde...\n')
            time.sleep(0.5)
            print(CIANO+"A acelereção media deste objeto e de",am,"metros por segundo")
            time.sleep(3)
            print("\n"*2)
        except ValueError:
            limpar_terminal()
            print(VERMELHO + "Erro:Digite um número válido (letras ou números decimais não são suportados).")
            time.sleep(2.5)
            print(AZUL + "Recarregando o programa...")
            time.sleep(1)
            limpar_terminal()
