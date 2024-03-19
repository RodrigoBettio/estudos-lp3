#If
#If condicao: 
idade = 20
if idade >= 18:
    print ("Maior de idade")

#if/else

idade = 20
if idade >= 18:
    print ("Maior de idade")
else:
    print ("Menor de idade")

#If/elif/else
if idade <= 12:
    print("Criança")
elif idade <= 17:
    print ("Adolescente")
elif idade <= 59:
    print ("Adulto")
else:
    print("Idoso")

#Exemplo de código aninhado (um dentro do outro)

email = "rodriguinho@gmail.com"
senha = "123"

if email == "rodriguinho@gmail.com":
    if senha == "123":
        print("Acesso Permitido")
    else: 
        print ("Acesso negado")
else:
    print ("Acesso negado")


#Código Corrigido
if email == "rodriguinho@gmail.com" and senha =="123":
    print("Acesso Permitido")
else:
    print ("Acesso negado")

#Operador Ternário 
idade = 20
if idade >= 18:
    status ="Maior de Idade"
else:
    status = "Menor de Idade" #Jeito errado 

status= "Maior de Idade" if idade >= 18 else "Menor de Idade"

#Match case

dia = 3
match dia:
    case 1:
        print ("Domingo")
    case 2:
        print ("Segunda")
    case 3:
        print ("Terça")
    case 4:
        print ("Quarta")
    case _:
        print ("Invalido")

match dia:
    case 1 | 7:
        print("Final de Semana")
    case 2 | 3 | 4 | 5 | 6:
        print("Dias de semana")
    case _:
        print("Dia inválido")
