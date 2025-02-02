#pg  Sn=A1.(Q**n-1)
import subprocess
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../libs')))
from Basics import *

while True:
    try:
        print(AMARELO + "-+-Digite (voltar) para voltar-+-\n")
        print(PADRAO + "Vamos Calcular a P.G")
        print("""Digite o valor de:
- A1 (primeiro numero da sequencia).
- Q (a razao da sequencia).
- N (numero de elementos na sequencia).
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
        Q = partes[1]
        N = int(partes[2])

        if Q == 1:
            Sn = A1 * N
        else:
            Sn = A1 * (Q**N - 1) / (Q - 1)

        limpar_terminal()
        print(CIANO + f"A soma dos {N} primeiros termos da P.G é: {Sn}\n\n")
        time.sleep(2.5)
        continue

    except Exception as e:
        limpar_terminal()
        print(VERDE+f"Erro: {e}")
        time.sleep(2.0)
        limpar_terminal()