#energia mecanica
#em = ep + ec
import time
import subprocess
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../libs')))
from Basics import *

while True:
    print(AMARELO+"-+-Digite (voltar) para voltar-+-\n")
    print(PADRAO+"Vamos Calculcar Energia Mecanica!")
    time.sleep(0.5)
    valores =  input("Qual a energia potencial e energia cinetica desse objeto?\n(escreva respectivamente separados por espaço).").lower()
    if valores == 'voltar':
        limpar_terminal()
        print(AMARELO + "\nVoltando...\n")
        time.sleep(1)
        limpar_terminal()
        subprocess.run(['python', 'physic_utils/energy/energy_hub.py'])
        break
    try:
        ep, ec = map(float, valores.split())
        em = ep + ec
        print(AMARELO+'calculando energia mecanica aguarde...\n')
        time.sleep(0.5)
        print(CIANO+f"-A energia mecanica deste objeto e de ",em,"N")
        time.sleep(3)
        print("\n"*2)
    except ValueError:
        limpar_terminal()
        print(VERMELHO + "Erro:Digite um número válido (letras não são suportadas).")
        time.sleep(2.5)
        print(AZUL + "Recarregando o programa...")
        time.sleep(1)
        limpar_terminal()