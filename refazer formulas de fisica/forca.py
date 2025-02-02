import time
import subprocess
while True:
    print("-+-Digite (voltar) para voltar-+-\n")
    print("Vamos Calcular Força!")
    time.sleep(0.5)
    valores = input("Qual a massa e aceleraçao do objeto?\n(escreva respectivamente dividido por espaço)").lower()
    if valores == 'voltar':
        print("\nVoltando...\n")
        time.sleep(1)
        subprocess.run(['python', 'mcm_hub.py'])
        break
    m, a = map(float, valores.split())
    f = m*a
    print()
    print(f"-A Força deste objeto e de ",f,"N")
    print()