import subprocess

while True:
    print("-+-Digite (voltar) para voltar-+-\n")
    print("CALCULAR ENERGIA")
    funcao = str(input("""Escolha uma função\n
- Energia Cinetica (EC)
- Energia Mecanica (EM)
- Energia Potencial Gravitacional (EPG)
- Energia Potencial Elastica (EPE) """)).strip().lower()
    #voltar
    if funcao == 'voltar':
        print("\nVoltando...\n")
        time.sleep(1)
        subprocess.run(['python', 'mcm_hub.py'])
        break
        
    # energia cinetica
    elif funcao == 'ec':
        subprocess.run(['python', 'physic/energy/ec.py'])
        break

    # energia mecanica
    elif funcao == 'em':
        subprocess.run(['python', 'physic/energy/em.py'])
        break

    # energia gravitacional
    elif funcao == 'epg':
        subprocess.run(['python', 'physic/energy/epg.py'])
        break

    # energia elastica
    elif funcao == 'epe':
        subprocess.run(['python', 'physic/energy/epe.py'])
        break

    else:
        print("\n"*100)
        print("\n== Erro:Função inexistente tente novamente ==\n\n")