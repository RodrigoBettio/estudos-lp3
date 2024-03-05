
#Identificadores 
#identificam aquilo com Letras e Números
#case sensitive
#palavras reservadas: Int, for, class
idade = 20
Idade = 20
#(São diferentes)

#Variável
#para definição de variáveis, definimos o identificador e o seu valor
#não precisamos definir tipo 
nome = "Mariazinha"

#Constante
#não existe constante
#o identificador deve ser por letra 
PI = 3.14

#Comentaŕio
'''
Comentário 
de 
Várias
Linhas 
'''
#Função
'''
def para definir que é uma função
: para identificar que terminou os paramêtros daquela função
'''
def somar(num1, num2):
    '''
    Não consegue rodar se não tiver identado 
    '''
    return num1 + num2

somar (10, 2)
somar ("Maria", true)
#Não vai rodar pois ele não consegue somar Maria com True, mas podemos passar qualquer valor como num1

