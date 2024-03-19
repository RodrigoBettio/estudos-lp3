#For, while, break, continue

#Operador in
for letra in "Python":
    print(letra)

itens = ["Banana", "Maça", "Pera" ]
for item in itens:
    print(item)

#range 
range (10)
list (range(10))
list (range(3, 10)) #Inicia no 3 e termina no 10
list (range(3, 10, 2)) #Inicia em 3, vai até 2, pulando de 2 em 2

for i in range (0, 11, 2):
    print(i)

#Para criar uma lista de 0 a 100
lista = list(range(100))

#type indica o tipo daquela variavel
#type (10) vai retornar int
#type (range(100)) vai retornar range
#type (list(range(100))) vai retornar list

#while
contador = 0 
while contador <= 5:
    print(contador)
    contador +=1

#break
numeros = [1, 3, 4, 5, 6, 8, 11]
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
        break #Vai encontrar o primeiro número par e parar a interação

#continue
numeros = [3, -1, 2, 0, -2]
for numero in numeros:
    if numero <= 0:
        continue
    print(numero) #Imprimir os números positivos

#mudar a lógica 
for numero in numeros:
    if numero >0:
        print(numero)

#Compressão de lista
#Forma concisa de criar listas em python
numeros = [2, 3, 4, 5, 6, 7]
quadrados = [] 

for numero in numeros:
    quadrados.append(numero **2) #Adiciona o numero ao quadrado com o append na lista quadrados

quadrados = [numero ** 2 for numero in numeros] #Faz a mesma coisa de maneira concisa

palavra = "Olá Rodriguinho"
letras = [letra for letra in palavra]
letras = [letra.upper() for letra in palavra] #Tudo em letra maiuscula. Podemos modificar as variaveis dentro da lista, essa manipulação é feita sempre antes do for

numeros [1, 2, 4, 5, 6]
pares = [numero for numero in numeros if numero % 2 == 0]