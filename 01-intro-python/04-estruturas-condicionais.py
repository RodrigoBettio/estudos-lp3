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
