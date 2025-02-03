#energia potencial gravitacional
#epg = m.g.h
import time
import subprocess
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../libs')))
from Basics import *

while True:
    print(AMARELO+"-+-Digite (voltar) para voltar-+-\n")
    print(PADRAO+"Vamos Calculcar Energia Potencial Gravitacional!")
    time.sleep(0.5)
    valores =  input("Qual a massa (Kg), aceleraçao gravitacional (m/s²) e altura (m) desse objeto?\n (escreva respectivamente separados por espaço).").lower()
    if valores == 'voltar':
        limpar_terminal()
        print(AMARELO + "\nVoltando...\n")
        time.sleep(1)
        limpar_terminal()
        subprocess.run(['python', 'physic_utils/energy/energy_hub.py'])
        break
    try:
        m,g,h = map(float, valores.split())
        epg = m*g*h
        print(AMARELO+'calculando energia potencial elastica aguarde...\n')
        time.sleep(0.5)
        print(CIANO+f"-A energia potencial gravitacional deste objeto e de ",epg,"N")
        time.sleep(3)
        print("\n"*2)
    except ValueError:
        limpar_terminal()
        print(VERMELHO + "Erro:Digite um número válido (letras não são suportadas).")
        time.sleep(2.5)
        print(AZUL + "Recarregando o programa...")
        time.sleep(1)
        limpar_terminal()