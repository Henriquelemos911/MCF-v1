import subprocess
import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../libs')))
from Basics import *

while True:
    print(AMARELO + "-+-Digite (voltar) para voltar-+-\n")
    time.sleep(0.5)
    print(PADRAO + "Vamos Calcular a Area e Perimetro do Circulo!")
    time.sleep(0.5)
    try:
            r = input("Digite o raio da circunferencia: ").lower()
            if r.lower( ) == 'voltar':
                subprocess.run(['python', 'math_utils/form/form_hub.py'])
                break
            else:
                r = float(r)
                area = 3.14 * r**2
                perimetro = 2*3.14*r
                
                print(CIANO + f"A area da circunferencia e de:{area}\ne seu perimetro e de:{perimetro}\n\n")
                time.sleep(2.5)
    except ValueError:
            limpar_terminal()
            print(VERMELHO + "Erro:Separe os números por espaço e tente novamente.")
            time.sleep(2.5)
            print(AZUL + "Recarregando o programa...")
            time.sleep(1)
            limpar_terminal()