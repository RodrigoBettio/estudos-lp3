#Tabuada de Um Número: Solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.

def tabuada():
    tabuada = []
    for i in range(1, 11):
        listaTabuada = numero * i
        tabuada.append(listaTabuada)
    return tabuada

def mostrarTabuada(listaTabuada):
    for i in listaTabuada:
        print(i)

numero = int(input("Digite o número que você quer a tabuada: "))
mostrarTabuada(tabuada())

print(tabuada())

