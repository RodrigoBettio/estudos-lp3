#Tipos de dados
# 1. Numérico
# int, float, complex

# int 
idade = 10

#float 
altura = 1.73

#2. Boolean
verdade = True
mentira = False

#3. String
#sequencia de caracteres 
nome = 'Maria'
nome = "Maria"

#multilinha 
frase = '''Olá mundo
isso 
foi só
um teste
 '''
print(frase)

#interpolação de string
nome = 'Maria'
idade = 23
frase = f"olá {nome}. Você tem {idade} anos"
print(frase)

#acesso de um caractere da string
nome ="Silvio Santos"
print (nome [0]) 
print (nome [-1]) #Pegar de trás para frente
print (nome [0:3]) #Pegar as 3 primeiras
print (nome.capitalize()) #Silvio santos
print (nome.upper())#SILVIO SANTOS

#4. List (também são objetos em python)
habilidades = []
habilidades = ['python', 'html', 'java'] 

#acessar
habilidades [1]

#adicionar 
habilidades.append('c#') #adiciona no final da lista
habilidades.insert (2, "CSS") #Adiciona o css na 2 posição
habilidades.insert (-1, "CSS") #Adiciona no penúltimo, se o programador quisesse inserir no último índice ele usaria append
print(habilidades)

for habilidade in habilidades: #Utilizamos no singular normalmente
    print(habilidade)

for habilidade in habilidades:
    print(habilidade, sep='o', end=',') #sep é o que separa cada um dos valores end é como ele encerra. Na documentação do print, ele coloca end='/n'

#5. Tupla
#Uma lista onde não podemos modificar nenhum item
#Utilizamos parenteses 
#Faça sempre uma lista, ao se perguntar se os valores não vão mudar, mude para uma tupla 

habilidades = ('python', 'html', 'java')

#6. Set
# Conjunto de valores
# Não permite elementos duplicados 
# Não é indexado
# Não tem índice 
# Utilizamos Chaves
habilidades = {'python', 'html', 'java', 'python'}

#7. dict (dicionario)
# Palavra -> definição
# Chave -> valor
# key -> value

nome = "Pedro Alves"
idade = 17
empregado = True

candidato = {
    'nome' : 'Pedro Alves',
    'idade' : 17,
    'empregado' : True
}

print (candidato['nome'])
print (candidato.keys)
print (candidato.values)

#8. None 
nome = None     
