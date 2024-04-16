#Simulador de Eleições: Crie um programa que simule uma votação com três candidatos. 
#O programa deve pedir ao usuário para votar várias vezes e, no final, 
#mostrar o número de votos de cada candidato e quem foi o vencedor.
def contabilizar_votos():
    candidato1 = []
    candidato2 = []
    candidato3 = []

    while True:
        print("\n### Eleição ###")
        print("Escolha o seu voto:")
        print("1 - Candidato 1")
        print("2 - Candidato 2")
        print("3 - Candidato 3")
        print("Qualquer outro número - Encerrar a votação")
        
        voto = int(input("Opção: "))
        if voto == 1:
            candidato1.append(voto)
        elif voto == 2:
            candidato2.append(voto)
        elif voto == 3:
            candidato3.append(voto)
        else:
            break
    
    return candidato1, candidato2, candidato3

def mostrar_resultados(candidato1, candidato2, candidato3):
    total_votos_candidato1 = len(candidato1)
    total_votos_candidato2 = len(candidato2)
    total_votos_candidato3 = len(candidato3)

    print(f"Total de votos do Candidato 1:{total_votos_candidato1}" )
    print(f"Total de votos do Candidato 2:{total_votos_candidato2}" )
    print(f"Total de votos do Candidato 3:{total_votos_candidato3}" )

    if total_votos_candidato1 > total_votos_candidato2 and total_votos_candidato1 > total_votos_candidato3:
        print("O Candidato 1 venceu a eleição!")
    elif total_votos_candidato2 > total_votos_candidato1 and total_votos_candidato2 > total_votos_candidato3:
        print("O Candidato 2 venceu a eleição!")
    elif total_votos_candidato3 > total_votos_candidato1 and total_votos_candidato3 > total_votos_candidato2:
        print("O Candidato 3 venceu a eleição!")
    else:
        print("Houve um empate entre os candidatos.")

def eleicoes():
    candidato1, candidato2, candidato3 = contabilizar_votos()
    mostrar_resultados(candidato1, candidato2, candidato3)

eleicoes()
