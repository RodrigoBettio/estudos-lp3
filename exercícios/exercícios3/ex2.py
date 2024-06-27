
#Entrada = Altura + peso
#Falar pro usuário quanto ele deve perder de peso

def menu():
    while True:
        print("----- CALCULADORA DE IMC -----")
        print("Digite o número da opção desejada:")
        print("1. Calcular IMC")
        print("2. Sair")
        print("------------------------------")
        opc = int(input(""))

        match opc :
            case 1:
                peso, altura, imc = calc_imc()
                classificacao(imc)
                calc_ganho_perda(peso, altura, imc)

            case 2:
                break
            case _:
                print("Digite uma opção válida. Tente Novamente.\n")

def calc_imc():
    altura = float(input("Qual é a sua altura?"))
    peso = float(input("Qual é o seu peso?"))
    if peso and altura > 0:
        imc = peso/(altura*altura)
    else: 
        "Digite seus dados corretamente"
        calc_imc()
    return peso, altura, imc

def classificacao(imc):
    if imc <= 18.5:
        print(f"Você está abaixo do Peso ideal. Seu imc é de {imc:.2f}")
    elif imc <= 24.9:
        print(f"Você está com o peso normal. Seu imc é de {imc:.2f}")
    elif imc <= 29.9:
        print(f"Você está com excesso de peso. Seu imc é de {imc:.2f}")
    elif imc <= 34.9:
        print(f"Você está com Obesidade de Classe 1. Seu imc é de {imc:.2f}")
    elif imc <= 39.9:
        print(f"Você está com Obesidade de Classe 2. Seu imc é de {imc:.2f}")
    else:
        print(f"Você está com Obesidade de Classe 3. Seu imc é de {imc:.2f}")
         
def calc_ganho_perda(peso, altura, imc): 
    peso_ideal_min = 18.5 *(altura*altura)
    peso_ideal_max = 24.9 *(altura*altura)
    if imc <= 18.5:
        peso_ganhar = peso_ideal_min - peso
        print(f"Você precisa ganhar {peso_ganhar:.2f}kg para atingir o peso ideal")
    elif imc >= 24.9: 
        peso_perder = peso_ideal_max - peso
        print(f"Você precisa perder {peso_perder:.2f}kg para atingir o peso ideal")
    else:
        print("")

menu()