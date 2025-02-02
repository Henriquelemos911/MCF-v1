import subprocess
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../libs')))
from Basics import *

while True:
    try:
        print(AMARELO + "-+-Digite (voltar) para voltar-+-\n")
        print(PADRAO + "Vamos Calcular a P.A")
        print("""Digite o valor de:
- A1 (primeiro termo da sequência).
- N (número de termos na sequência).
- R (razão da sequência).
Respectivamente separados por espaço""")
        valores = input(AMARELO + "").strip()
        
        if valores.lower() == 'voltar':
            limpar_terminal()
            print(AMARELO + "\nVoltando...\n")
            time.sleep(1)
            limpar_terminal()
            subprocess.run(['python', 'math_utils/pga/pga_hub.py'])
            break
        
        partes = valores.split()
        
        if len(partes) != 3:
            limpar_terminal()
            print(VERMELHO + "Erro: Por favor, insira exatamente 3 valores.")
            time.sleep(2.5)
            print(AZUL + "Recarregando o programa...")
            time.sleep(1)
            limpar_terminal()
            continue
        
        try:
            partes = [float(val) for val in partes]
        except ValueError:
            limpar_terminal()
            print(VERMELHO + "Erro: Por favor, insira números válidos.")
            time.sleep(2.5)
            print(AZUL + "Recarregando o programa...")
            time.sleep(1)
            limpar_terminal()
            continue

        A1 = partes[0]
        N = int(partes[1])
        R = partes[2]

        Sn = (N / 2) * (2 * A1 + (N - 1) * R)

        limpar_terminal()
        print(CIANO + f"A soma dos {N} primeiros termos da P.A é: {Sn}")
        time.sleep(2.5)
        continue

    except Exception as e:
        limpar_terminal()
        print(VERDE+f"Erro: {e}")
        time.sleep(2.0)
        limpar_terminal()