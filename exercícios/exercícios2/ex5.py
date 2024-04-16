#Verificador de Palíndromos: Solicite ao usuário que digite uma palavra ou frase e 
#verifique se é um palíndromo (ou seja, pode ser lida de frente para trás e de trás para frente da mesma forma).

def palindromo():
    palavra = input("Digite uma palavra para verificarmos se é um palíndromo ou não: ")
    return palavra

def verificadorPalindromo(palavra):
    palavra = palavra.lower()  
    if palavra == palavra[::-1]:  
        return True
    else:
        return False

def mostrarPalindromo():
    palavra = palindromo()
    if verificadorPalindromo(palavra):
        print("A palavra/frase é um palíndromo!")
    else:
        print("A palavra/frase não é um palíndromo.")

mostrarPalindromo()

