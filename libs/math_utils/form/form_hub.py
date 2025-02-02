#FORM HUB
import subprocess
import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../libs')))
from Basics import *

limpar_terminal()
print(VERDE + "Area e Perimetro HUB")
while True:
    print(AMARELO + "-+-Digite (voltar) para voltar-+-")
    time.sleep(0.5)
    print(PADRAO + "Qual a forma que deseja calcular?")
    print(CIANO + """
- Quadrado (Q)
- Retângulo (R)
- Triângulo (T)
- Losango (L)
- Círculo (C)""")
    form = str(input(PADRAO + "")).strip().lower()
    limpar_terminal()
    if form == 'voltar':
        subprocess.run(['python', 'mcf_hub.py'])
   
    elif form == 'q':
        subprocess.run(['python', 'math_utils/form/square.py'])
        
    elif form == 'r':
        subprocess.run(['python', 'math_utils/form/rectangle.py'])
        
    elif form == 't':
        subprocess.run(['python', 'math_utils/form/triangle.py']) 
        
    elif form == 'l':
        subprocess.run(['python', 'math_utils/form/diamond.py'])
        
    elif form == 'c':
        subprocess.run(['python', 'math_utils/form/circle.py'])
        
    else:
        print("Erro:Função inexistente tente novamente.")
        limpar_terminal()
        print(VERMELHO + "Erro:Função inexistente.")
        time.sleep(2.5)
        print(AZUL + "Recarregando o programa...")
        time.sleep(1)
        limpar_terminal()