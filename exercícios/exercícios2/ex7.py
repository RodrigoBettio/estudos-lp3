# Jogo da Forca: Implemente uma versão simples do jogo da forca. 
#O programa começa com uma palavra oculta (o usuário não vê) e 
#o usuário tenta adivinhar a palavra, letra por letra. 
#O usuário tem um número limitado de tentativas para adivinhar toda a palavra.
import random
def escolherPalavra():
    palavras = ["python", "programacao", "computador", "teclado", "mouse", "monitor"]
    return random.choice(palavras)

def forca():
    palavra = escolherPalavra()
    letras_usuario = []
    chances = 7

    while True:
        for letra in palavra:
            if letra in letras_usuario:
                print (letra, end=" ")
            else:
                print("_", end=" ")
        
        print("")
        print("### Jogo da Forca ###")
        print("**Escreva em minusculo por favor")
        print("")
        print(f"Voce tem {chances} chances")
        print(f"Essas letras já foram utilizadas: {letras_usuario}")
        print("")
        tentativa = input("Tente adivinhar uma letra para a palavra:")
        letras_usuario.append(tentativa)

        if tentativa not in palavra:
            chances -= 1

        ganhou = True
        for letra in palavra:
            if letra not in letras_usuario:
                ganhou = False

        if chances == 0 or ganhou:
            break

    if ganhou:
        print(f"Parabens, você ganhou restando {chances} chances, a palavra era: {palavra}")
        
    else:
        print(f"Acabaram suas chances, você perdeu, a palavra era:{palavra}")
        
            
forca()