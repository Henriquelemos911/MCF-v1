import subprocess
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../libs')))
from Basics import *

def formula_delta(A, B, C):
    delta = B**2 - 4*A*C
    return delta
    
while True:
    print(AMARELO + "-+-Digite (voltar) para voltar-+-\n")
    print(PADRAO + "Vamos Calcular Bhaskara")
    time.sleep(0.5)
    try:
        print("Primeiramente vamos descobrir o valor de delta: ")
        A_input = input("Qual o valor de A?: ").strip()
        if A_input.lower() == "voltar":
            print(AMARELO + "\nVoltando...\n")
            time.sleep(1)
            subprocess.run(["python", "mcf_hub.py"])
            break
        A = float(A_input)
        B_input = input("Qual o valor de B?: ").strip()
        if B_input.lower() == "voltar":
            print(AMARELO + "\nVoltando...\n")
            time.sleep(2.5)
            limpar_terminal()
            subprocess.run(["python", "mcf_hub.py"])
            break
        B = float(B_input)
        C_input = input("Qual o valor de C?: ").strip()
        if C_input.lower() == "voltar":
            print(AMARELO + "\nVoltando...\n")
            time.sleep(1)
            subprocess.run(['python', 'mcf_hub.py'])
            break
        C = float(C_input)
        delta = formula_delta(A, B, C)
        print(f"O valor de delta é: {delta}")
        time.sleep(0.5)
        print("\nOtimo! Estamos quase lá, agora vamos descobrir as raizes da equação: ")
        print("Estamos calculando o valor de X1 e X2 aguarde...\n")
        time.sleep(1)
        if delta < 0:
            print("A equação não possui raizes reais.\n")
            time.sleep(2.5)
        elif delta == 0:
            x1 = (-B + delta**0.5) / (2*A)
            print(f"A equação possui apenas uma raiz real: {x1}\n")
            time.sleep(2.5)
        else:
            x1 = (-B + delta**0.5) / (2*A)
            x2 = (-B - delta**0.5) / (2*A)
            print(f"A equação possui duas raizes reais: {x1} e {x2}\n")
            time.sleep(2.5)
    except ValueError:
        limpar_terminal()
        print(VERMELHO + "Erro:Digite números válidos (letras não são suportadas)")
        time.sleep(2.5)
        print(AZUL + "Recarregando o programa...")
        time.sleep(1)
        limpar_terminal()