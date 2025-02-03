import subprocess
import time
import sys
import os
from libs.Basics import *

while True:
    try:
# MENU PRINCIPAL
        limpar_terminal()
        print(VERDE + "      Tela Inicial MCF      v1")
        print(PADRAO + "Escolha uma função (digite o codigo)")
        print(CIANO + """----Formulas Matematicas----
- Calcular P.G / P.A (PGA)
- Calcular area / perimetro de uma forma(AP)
- Teorema de Pitagoras (TP)
- Calcular Media (MD)
- Calcular Fatorial (FT)
- Calcular Raiz Quadrada (SQRT)
- Calcular Bhaskara (BK)
- ####### (##)
----Formulas de Fisica----
- Calcular Energia (CE) ##
- Calcular Movimento (CM) ##
- Calcular Força (CF) ##
- ####### (##)
- ####### (##)""")
        # PEGAR A FUNÇÃO DESEJADA
        funcao = str(input(PADRAO + "Onde deseja ir? ")).strip().upper()
        limpar_terminal()
        print(VERDE + f"\nCarregando {funcao} aguarde...")
        time.sleep(2.0)
        limpar_terminal()
        funcao = funcao.lower()
# DIRECIONA O USUARIO PARA A FUNÇÃO ESCOLHIDA
    # FUNÇÕES SOBRE MATEMATICA
        # P.G / P.A
        if funcao == 'pga':
            subprocess.run(['python', 'math_utils/pga/pga_hub.py'])
            break
        # AREA / PERIMETRO
        elif funcao == 'ap':
            subprocess.run(['python', 'math_utils/form/form_hub.py'])
            break
        # TEOREMA DE PITAGORAS
        elif funcao == 'tp':
            subprocess.run(['python', 'math_utils/pit/pit_hub.py'])
            break
        # CALCULAR MEDIA
        elif funcao == 'md':
            subprocess.run(['python', 'math_utils/media.py'])
            break
        # CALCULAR RAIZ QUADRADA
        elif funcao == 'sqrt':
            subprocess.run(['python', 'math_utils/sqrt.py'])
            break
        # CALCULAR FATORIAL
        elif funcao == 'ft':
            subprocess.run(['python', 'math_utils/fatorial.py'])
            break
        # CALCULAR BHASKARA
        elif funcao == 'bk':
            subprocess.run(['python', 'math_utils/bhaskara.py'])
            break
    # FUNCÕES SOBRE FISICA
        # CALCULAR ENERGIA
        elif funcao == 'ce':
            subprocess.run(['python', 'physic_utils/energy/energy_hub.py'])
            break
        # CALCULAR MOVIMENTO
        elif funcao == 'cm':
            subprocess.run(['python', 'physic_utils/mov/mov_hub.py'])
            break
        # CALCULAR FORÇA
        elif funcao == 'cf':
            subprocess.run(['python', 'physic_utils/forca.py'])
            break

    # TRATAMENTO DE ERROS
        # FUNÇÃO INDISPONIVEL OU AINDA NÃO CRIADA. (DEV EDITION APENAS!.)
        elif funcao == '##':
            print(VERMELHO + "Erro:Ops você digitou uma ação que ainda não existe ou está indisponível,tente novamente.")
            time.sleep(0.5)
            print(AZUL + "Recarregando o programa...")
            time.sleep(2.0)
            limpar_terminal()
            continue
        # FUNÇAO INEXISTENTE
        else:
            print(VERMELHO + "Erro:Função inexistente aguarde e tente novamente.")
            time.sleep(0.5)
            print(AZUL + "Recarregando o programa...")
            time.sleep(2.0)
            limpar_terminal()
            continue
    except Exception as e:
        print(VERDE+f"Erro:{e}")
        time.sleep(2.0)
        limpar_terminal()