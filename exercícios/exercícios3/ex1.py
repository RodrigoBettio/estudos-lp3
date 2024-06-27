#Entrada : Comprimento, altura e largura de um aquário

#Calcular: Volume, Potência do Termostato, Quantidade de litros na filtragem

#Volume é comprimento*altura*largura/1000
#Termostato é potencia = volume*0,05*(temperatura desejada - temperatura ambiente)
#Quantidade de filtragem no mínimo 2 a 3x o volume do aquário

def menu():
    while True:
        print("----- AQUÁRIO -----")
        print("Digite o número da opção desejada")
        print("1. Calcular o Volume")
        print("2. Calcular a Potência do Termostato")
        print("3. Calcular a quantidade de filtragem mínima")
        print("4. Sair") 
        print("-------------------")

        opc = int(input(""))
        match opc:
            case 1:
                comprimento, altura, largura = infos()
                volume = calc_vol(comprimento, altura, largura)
                print(f"O volume do seu aquário é de {volume}litros")
            case 2:
                potencia(volume)
            case 3:
                filtragem(volume)
            case 4:
                print("Saindo do Programa...")
                break
            case _:
                print("Escolha um número de 1 a 4")

def infos():
    print("Vamos precisar de algumas informações do seu aquário...")
    comprimento = float(input("Digite o valor para o comprimento: "))
    altura = float(input("Digite o valor para a altura: "))
    largura = float(input("Digite o valor para a largura: \n"))
    return comprimento, altura, largura

def calc_vol(comprimento, altura, largura):
    volume = (comprimento*altura*largura)/1000
    return volume

def potencia(volume):
    if volume <= 0:
        print("Você precisa calcular o volume primeiro")
        menu()
    else: 
        temp_desejada = float(input("Qual é a temperatura desejada para o aquário (Apenas o número)\n"))
        temp_ambiente = float(input("Qual é a temperatura atual do ambiente?"))
        potencia = volume*0.05*(temp_desejada - temp_ambiente)
        print(f"A potência do seu termostato deve ser de: {potencia}")

def filtragem(volume):
    if volume <= 0:
        print("Você precisa calcular o volume primeiro")
        menu()
    else:
        filtragem = volume*3 
        print(f"Deve-se filtrar o filtro {filtragem} por hora")


menu()
