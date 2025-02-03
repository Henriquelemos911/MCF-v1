#energia cinetica
#ec = m.v2 /2
import subprocess
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../libs')))
from Basics import *

while True:
    print(AMARELO+"-+-Digite (voltar) para voltar-+-\n")
    print(PADRAO+"Vamos Calcular Energia Cinetica!")
    time.sleep(0.5)
    valores = input("Qual a massa e velocidade (m/s) do objeto?\n(escreva respectivamente dividido por espaço)").lower()
    if valores == 'voltar':
        limpar_terminal()
        print(AMARELO + "\nVoltando...\n")
        time.sleep(1)
        limpar_terminal()
        subprocess.run(['python', 'physic_utils/energy/energy_hub.py'])
        break
    try:
        m, v = map(float, valores.split())
        v2 = v**2
        ec =m*v2 /2
        print(AMARELO+'calculando energia cinetica aguarde...\n')
        time.sleep(0.5)
        print(CIANO+f"-A energia cinetica deste objeto e de ",ec,"N")
        time.sleep(3)
        print("\n"*2)
    except ValueError:
        limpar_terminal()
        print(VERMELHO + "Erro:Digite um número válido (letras não são suportadas).")
        time.sleep(2.5)
        print(AZUL + "Recarregando o programa...")
        time.sleep(1)
        limpar_terminal()
