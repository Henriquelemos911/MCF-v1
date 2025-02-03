import subprocess
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../libs')))
from Basics import *

while True:
    print(AMARELO+"-+-Digite (voltar) para voltar-+-\n")
    time.sleep(0.5)
    print(PADRAO+"Vamos Calcular a Area do Retangulo!")
    try:
            valores = input("Digite a base e altura do retângulo separados por espaço: ")
            if valores == 'voltar':
                subprocess.run(['python', 'math_utils/form/form_hub.py'])
                break
            else:
                base, altura = map(float, valores.split())
                if base == altura:
                    print("A base não pode ser igual a altura!")
                    time.sleep(2.5)
                    limpar_terminal()
                    continue
                area = base * altura
                perimetro = 2 * (base + altura)
                print(CIANO+f"A área do retângulo é de {area}\nE seu perímetro é de {perimetro}\n\n")
                time.sleep(2.5)
    except ValueError:
            limpar_terminal()
            print(VERMELHO + "Erro:Separe os números por espaço e tente novamente.")
            time.sleep(2.5)
            print(AZUL + "Recarregando o programa...")
            time.sleep(1)
            limpar_terminal()