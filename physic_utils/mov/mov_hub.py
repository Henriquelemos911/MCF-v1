import subprocess
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../libs')))
from Basics import *

while True:
    print(AMARELO+"-+-Digite (voltar) para voltar-+-\n")
    print("Escolha uma função")
    funcao = str(input(CIANO+"""
- Movimento Uniforme (MU)
- Movimento Uniforme Variado(MUV)
- Aceleração Media (AM)
- Velocidade Media (VM) """)).strip().lower()
    
    if funcao == 'voltar':
        if funcao == 'voltar':
        limpar_terminal()
        print(AMARELO + "\nVoltando...\n")
        time.sleep(1)
        limpar_terminal()
        subprocess.run(['python', 'mcf_hub.py'])
        

    elif funcao == 'mu':
        limpar_terminal()
        print(VERDE + "Carregando movimento uniforme aguarde...")
        time.sleep(2.0)
        limpar_terminal()
        subprocess.run(['python', 'physic_utils/mov/mu.py'])
        break

    
    elif funcao == 'muv':
        limpar_terminal()
        print(VERDE + "Carregando movimento uniforme variado aguarde...")
        time.sleep(2.0)
        limpar_terminal()
        subprocess.run(['python', 'physic_utils/mov/muv.py'])
        break

    
    elif funcao == 'am':
        limpar_terminal()
        print(VERDE + "Carregando aceleração media aguarde...")
        time.sleep(2.0)
        limpar_terminal()
        subprocess.run(['python', 'physic_utils/mov/acel_media.py'])
        breaka

   
    elif funcao == 'vm':
        limpar_terminal()
        print(VERDE + "Carregando velocidade media aguarde...")
        time.sleep(2.0)
        limpar_terminal()
        subprocess.run(['python', '/physic_utils/mov/velo_media.py'])
        break

    else:
        print("Erro:Função inexistente tente novamente.")
        limpar_terminal()
        print(VERMELHO + "Erro:Função inexistente.")
        time.sleep(2.5)
        print(AZUL + "Recarregando o programa...")
        time.sleep(1)
        limpar_terminal()