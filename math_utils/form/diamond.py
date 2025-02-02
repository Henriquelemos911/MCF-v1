import subprocess
import math
import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../libs')))
from Basics import *

while True:
    print(AMARELO + "-+-Digite (voltar) para voltar-+-\n")
    time.sleep(0.5)
    print(PADRAO  + "Vamos Calcular a Area e Perimetro do Losango!")
    try:
            valores = input("Digite o Diametro maior e o Diametro menor do losango separados por espaço: ")
            if valores == 'voltar':
                subprocess.run(['python', 'math_utils/form/form_hub.py'])
                break
            else:
                D,d = map(float, valores.split())
                area = D*d / 2
                percat1 = D / 2
                percat2 = d / 2
                ladoC = D**2 + d**2
                lado = math.sqrt(ladoC)
                perimetro = lado * 2
                print(CIANO + f"A área do losango é de {area}\ne seu perimetro e de {perimetro}\n\n")
                time.sleep(2.5)
    except ValueError:
            limpar_terminal()
            print(VERMELHO + "Erro:Separe os números por espaço e tente novamente.")
            time.sleep(2.5)
            print(AZUL + "Recarregando o programa...")
            time.sleep(1)
            limpar_terminal()