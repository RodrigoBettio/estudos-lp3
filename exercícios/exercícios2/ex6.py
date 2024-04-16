#Conversor de Notas Escolares: Baseado em uma pontuação fornecida pelo usuário (0 a 100), 
#converta para o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns.

def conversor_notas(notas):
    if notas >= 90:
        return 'A'
    elif notas >= 80:
        return 'B'
    elif notas >= 70:
        return 'C'
    elif notas >= 60:
        return 'D'
    else:
        return 'F'

def mostrar_resultado():
    notas = float(input("Digite a pontuação (0 a 100): "))
    if notas < 0 or notas > 100:
        print("Pontuação inválida. Por favor, digite uma pontuação entre 0 e 100.")
    else:
        nota = conversor_notas(notas)
        print(f"A nota correspondente a pontuação {notas} é: {nota}")

mostrar_resultado()
