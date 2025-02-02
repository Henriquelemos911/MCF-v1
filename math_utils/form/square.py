import subprocess
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../libs')))
from Basics import *

while True:
    print(AMARELO+"-+-Digite (voltar) para voltar-+-\n")
    time.sleep(0.5)
    print(PADRAO+"Vamos Calcular a Area do Quadrado!")
    try:
        lado = input("Qual o tamanho do lado do quadrado?  ")
        if lado == 'voltar':
            subprocess.run(['python', 'math_utils/form/form_hub.py'])
            break
        else:
              lado = float(lado)
              area = lado * lado
              perimetro = lado * 4
              print(CIANO+f"A área do quadrado é de: {area}\nE seu perímetro é de: {perimetro}\n\n")
              time.sleep(2.5)
    except ValueError:
            limpar_terminal()
            print(VERMELHO + "Erro:Digite uma base valida.")
            time.sleep(2.5)
            print(AZUL + "Recarregando o programa...")
            time.sleep(1)
            limpar_terminal()