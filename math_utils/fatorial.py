import subprocess
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../libs')))
from Basics import *

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

while True:
    print(AMARELO + "-+-Digite (voltar) para voltar-+-\n")
    print(PADRAO + "Vamos Calcular Um Número Fatorial")
    try:
        numero = input("Digite um número que deseja descobrir seu fatorial: ").strip()
        if numero.lower() == 'voltar':
            print(AMARELO + "\nVoltando...\n")
            time.sleep(2.5)
            limpar_terminal()
            subprocess.run(['python', 'mcf_hub.py'])
            break  
        numero = int(numero)
        if numero < 0:
            print("\nO fatorial não é definido para números negativos.\n")
        else:
            print(f"Calculando aguarde...\n")
            time.sleep(0.5)
            print(f"\nO fatorial de {numero} é {fatorial(numero)}\n\n")
        time.sleep(1)
    except ValueError:
        limpar_terminal()
        print(VERMELHO + "Erro:Digite um número válido (letras ou números decimais não são suportados).")
        time.sleep(2.5)
        print(AZUL + "Recarregando o programa...")
        time.sleep(1)
        limpar_terminal()
