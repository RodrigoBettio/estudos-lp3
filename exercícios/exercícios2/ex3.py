#Contador de Vogais e Consoantes: Peça ao usuário para digitar uma frase e 
#retorne o número de vogais e consoantes na frase.

def contador(frase):
    vogais = "aeiou"
    numVogais = 0
    numConso = 0

    letras = [letra for letra in frase.strip()]
    
    for i in letras:
        if i in vogais:
            numVogais += 1
        else:
            numConso += 1

    return numConso, numVogais

frase = input("Digite uma frase para contarmos as vogais e consoantes:")
contador(frase)
numConso, numVogais = contador(frase)
print(f"Consoantes: {numConso} e Vogais: {numVogais}")
