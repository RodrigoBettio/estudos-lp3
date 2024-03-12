#Operadores Aritméticos
#  +,  -,  /,  *, %, ** (Potenciação)

numero = 10
elevado_quadrado = numero ** 2 #Numero elevado ao quadrado

#Operadores Lógicos
#and, or, not
# print(2+3) devolve um int
# Os operadores lógicos devolvem um boolean

print (TRUE and FALSE) # False
print (TRUE or FALSE) #True
print (TRUE not FALSE)#True

#Operadores de Comparaçãoo
# ==, !=, >, <, >=, <=

# Operador is, is not
#São operadores de identidade 
#Compara se os objetos são os mesmos
#Verifica se ocupa o mesmo espaço de memória 

a = [1, 2, 3]
b = [1, 2, 3]

print (a == b) #true
print (a is b) #false
c = b 
print (c is b) #true

#Operador in, not in
#Usado para ver se o elemento já existe naquela sequência

opcoes = ("sim", "não", "talvez")
opcao = input ("Digite uma opção")
opcao = opcao.lower().strip(); #Lower para transformar tudo em minusculo, strip para remover os espaços
if opcao in opcoes:
    print("Ok")
else:
    print("invalido")