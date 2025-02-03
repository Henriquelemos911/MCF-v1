import subprocess
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../libs')))
from Basics import *

while True:
    print(AMARELO+"-+-Digite (voltar) para voltar-+-\n")
    time.sleep(0.5)
    print(PADRAO+"Escolha uma função")
    funcao = str(input(CIANO+"""
- Energia Cinetica (EC)
- Energia Mecanica (EM)
- Energia Potencial Gravitacional (EPG)
- Energia Potencial Elastica (EPE) """)).strip().lower()
    #voltar
    if funcao == 'voltar':
        limpar_terminal()
        print(AMARELO + "\nVoltando...\n")
        time.sleep(1)
        limpar_terminal()
        subprocess.run(['python', 'mcf_hub.py'])
        
    # energia cinetica
    elif funcao == 'ec':
        limpar_terminal()
        print(VERDE + "Carregando energia cinetica aguarde...")
        time.sleep(2.0)
        limpar_terminal()
        subprocess.run(['python', 'physic_utils/energy/ec.py'])
        break

    # energia mecanica
    elif funcao == 'em':
        limpar_terminal()
        print(VERDE + "Carregando energia mecanica aguarde...")
        time.sleep(2.0)
        limpar_terminal()
        subprocess.run(['python', 'physic_utils/energy/em.py'])
        break

    # energia gravitacional
    elif funcao == 'epg':
        limpar_terminal()
        print(VERDE + "Carregando energia potencial gravitacional aguarde...")
        time.sleep(2.0)
        limpar_terminal()
        subprocess.run(['python', 'physic_utils/energy/epg.py'])
        break

    # energia elastica
    elif funcao == 'epe':
        limpar_terminal()
        print(VERDE + "Carregando energia potencial elastica aguarde...")
        time.sleep(2.0)
        limpar_terminal()
        subprocess.run(['python', 'physic_utils/energy/epe.py'])
        break

    else:
        print("Erro:Função inexistente tente novamente.")
        limpar_terminal()
        print(VERMELHO + "Erro:Função inexistente.")
        time.sleep(2.5)
        print(AZUL + "Recarregando o programa...")
        time.sleep(1)
        limpar_terminal()