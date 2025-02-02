import subprocess

while True:
    print("-+-Digite (voltar) para voltar-+-\n")
    print("      CALCULAR MOVIMENTO      ")
    funcao = str(input("""   Escolha uma função\n
- Movimento Uniforme (MU)
- Movimento Uniforme Variado(MUV)
- Aceleração Media (AM)
- Velocidade Media (VM) """)).strip().lower()
    
    if funcao == 'voltar':
        print("\nVoltando...\n")
        time.sleep(1)
        subprocess.run(['python', 'mcm_hub.py'])
        break
        

    elif funcao == 'mu':
        subprocess.run(['python', 'physic/mov/mu.py'])
        break

    
    elif funcao == 'muv':
        subprocess.run(['python', 'physic/mov/muv.py'])
        break

    
    elif funcao == 'am':
        subprocess.run(['python', 'physic/mov/acel_media.py'])
        break

   
    elif funcao == 'vm':
        subprocess.run(['python', '/physic/mov/velo_media.py'])
        break

    else:
        print("\n"*100)
        print("\n== Erro:Função inexistente tente novamente ==\n\n")