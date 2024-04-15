#Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 
#que o programa escolheu aleatoriamente. Informe ao usuário se o palpite está alto ou baixo, 
#até que ele acerte o número.

import random
def jogoDeAdivinhacao():
    numero = random.randint(1,100)

    print ("Olá, seja Bem Vindo ao Jogo da Adivinhação")
    print ("O programa escolheu um número e 0 a 100, tente acertá-lo e diremos se você está perto ou não")
    
    while True:
        palpite = int(input("Digite seu Palpite:"))
        if palpite < numero:
            print("Seu palpite está muito baixo")

        elif palpite > numero:
            print("Seu palpite está muito alto")

        else:
            print("Parabéns, você acertou") 
            break
jogoDeAdivinhacao()