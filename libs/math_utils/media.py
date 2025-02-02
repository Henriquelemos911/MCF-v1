from collections import Counter
import subprocess
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../libs')))
from Basics import *

def calcular_mediana(lista):
    lista.sort()
    quantidade = len(lista)
    
    if quantidade % 2 == 0:
        mediana = (lista[quantidade // 2 - 1] + lista[quantidade // 2]) / 2
    else:
        mediana = lista[quantidade // 2]
        
    return mediana

def calcular_moda(lista):
    contador = Counter(lista)
    moda = contador.most_common(1)[0] 
    return moda[0], moda[1] 

while True:
    print(AMARELO + "-+-Digite (voltar) para voltar-+-\n")
    print(PADRAO + "Vamos Calcular a média De Uma Lista")
    time.sleep(0.5)
    try:
        print("Digite sua lista separada por espaço.")
        entrada = input(AMARELO + "").split()
        
        if entrada == ['voltar']:
            print(AMARELO + "\nVoltando...\n")
            time.sleep(2.5)
            limpar_terminal()
            subprocess.run(['python', 'mcf_hub.py'])
            continue
        
        if len(entrada) == 0:
            print(VERMELHO + "Erro: listas vazias não são suportadas tente novamente!.")
            time.sleep(2.5)
            print(AZUL + "Recarregando o programa...")
            time.sleep(1)
            limpar_terminal()
            continue
            
        lista = [float(num) for num in entrada]
        
        quantidade = len(lista)
        
        soma = sum(lista)
        
        media = soma / quantidade
        
        mediana = calcular_mediana(lista)
        
        moda_valor, moda_contagem = calcular_moda(lista)
        print(PADRAO + f"Calculando aguarde...\n")
        time.sleep(0.5)
        print(CIANO + f"A sua média é: {media}\n")
        print(CIANO + f"A sua lista em ordem crescente é: {sorted(lista)}\n")
        print(CIANO + f"A sua mediana é: {mediana}\n")
        print(CIANO + f"O número que mais se repete (moda) é: {moda_valor} (repetido {moda_contagem} vezes)")
        print(PADRAO + "\n")
        
    except ValueError:
        limpar_terminal()
        print(VERMELHO + "Erro:Digite uma lista com numeros(letras não são suportadas).")
        time.sleep(2.5)
        print(AZUL + "Recarregando o programa...")
        time.sleep(1)
        limpar_terminal()