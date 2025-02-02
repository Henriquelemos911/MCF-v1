#acel media
# am= ∆v / ∆t
import time
import subprocess
while True:
    try:
        print("-+-Digite (voltar) para voltar-+-\n")
        print("Vamos Calcular Aceleração Media!")
        time.sleep(0.5)
        valores = input("Qual a variação de velocidade (m/s) e o tempo de intervalo a se calcular?\n(escreva respectivamente dividido por espaço)").lower()
        
        if valores == 'voltar':
            print("\nVoltando...\n")
            time.sleep(1)
            subprocess.run(['python', 'physic/mov/mov_hub.py'])
            continue
        v,t = map(float, valores.split())
        am = v / t
        print("\nA acelereção media deste objeto e de",am,"metros por segundo\n\n")
    except ValueError:
            print("Erro:digite numeros validos ou uma ação existente!")