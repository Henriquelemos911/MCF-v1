import subprocess
import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../libs')))
from Basics import *

while True:
    print(AMARELO+"-+-Digite (voltar) para voltar-+-\n")
    print(PADRAO+"Vamos Calcular a Area do Triangulo")
    try:
            valores = input("Digite a base e altura do triangulo separados por espaço: ").lower()
            if valores == 'voltar':
                subprocess.run(['python', 'math_utils/form/form_hub.py'])
                break
            else:
                base, altura = map(float, valores.split())
                area = base * altura / 2
                print(CIANO+f"A área do triangulo é de {area}\n\n")
                time.sleep(2.5)
    except ValueError:
            limpar_terminal()
            print(VERMELHO + "Erro:Separe os números por espaço e tente novamente.")
            time.sleep(2.5)
            print(AZUL + "Recarregando o programa...")
            time.sleep(1)
            limpar_terminal()