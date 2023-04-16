""" Curso Introdutório Completo de Python
    Aquecimento PSW 6.0 #07
"""
print("#### Olá, Mundo! ####")
print('\n')


""" Variáveis básicas: 
No Python as variáveis são definidas de acordo como 
são informados os dados em suas variáveis
int: 10, 1000, -9900, -2500
float: 10.5, 150.543, 1000.1, -2.5
string: 'Caio', "Aula no Youtube", 'VSCode', '10.87'
bool: True ou False
"""
print("#### Variáveis Básicas ####")
nome = 'Kuruvar'                        # variável informada com cadeia de caracteres
idade = 32                              # variárvel informada com número inteiro
# identificar variáveis com type(var)

print(f"Variável 'nome': {nome}.")
print(f"Variável 'idade': {idade}.")
print('\n')

""" Saída interpolada: 
em versões mais recentes do Python é recomendado usar 
'f' antes do início da string do print
"""
print("#### Saída Interpolada ####")
print(f"O meu nome é {nome} e minha idade é {idade}.")
print('\n')


""" Entradas de dados: 
informar o 'input("Mensagem")' dentro de uma 
variável para receber um dado em uma variável
"""
print("#### Entrada de dados ####")
nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
print (f"Olá, {nome}, a idade digitada é: {idade}.")
print('\n')


""" Conversão de dados: 
para converter dados entre strings ou valores
exemplo: int() -> faz conversão do dado entre o parênteses para int
 >-> tudo que é informado pelo input() é incluído como string
então será necessário usar a conversão de dados para tipo que precisa
Exemplo: float(input('Mensagem'))
"""
print("#### Conversão de Dados ####")
prova1 = 9.9
prova2 = 9.8
somatoria = int(prova1) + int(prova2)

# também pode ser feita a conversão durante a manipulação dos dados
# somatoria = float(prova1) + float(prova2)
print(f"Somatória das provas é: {somatoria}.")
print('\n')


""" Operadores Matemáticos: 
Operadores: [+, -, *, **, /, //, %]
Ordem de precedência: ** -> * -> / -> // -> % -> + -> -
Precedência: dentro do parênteses -> fora do parênteses
Da esquerda para a direita
"""
print("#### Operadores Matemáticos ####")
prova1 = 10
prova2 = 9
media = (prova1 + prova2) / 2

# divisão por inteiro são duas barras //

print(f"A média das provas é: {media:.2f}.")
# na interpolação a variável pode ser formatada com :.2f
# sendo o 'f' o tipo da variável
# e a quantidade de caracteres em :X.X
print('\n')


""" Operadores Relacionais: 
Operadores: (==, >, <, >=, <=)
"""
print("#### Operadores Relacionais ####")
prova1 = 10
prova2 = 5

resultado = prova1 == prova2
print(f"Resultado da comparação == das provas é: {resultado}.")
resultado = prova1 < prova2
print(f"Resultado da comparação < das provas é: {resultado}.")
resultado = prova1 <= prova2
print(f"Resultado da comparação <= das provas é: {resultado}.")
resultado = prova1 > prova2
print(f"Resultado da comparação > das provas é: {resultado}.")
resultado = prova1 >= prova2
print(f"Resultado da comparação >= das provas é: {resultado}.")
print('\n')


""" Operadores lógicos:
Operadores: [and, or, not]
"""
print("#### Operadores Lógicos ####")
prova1 = True
prova2 = False

resultado = prova1 and prova2
print(f"Resultado da comparação AND das provas é: {resultado}.")
resultado = prova1 or prova2
print(f"Resultado da comparação OR das provas é: {resultado}.")
resultado = not prova2
print(f"not da prova1 é: {resultado}.")
print('\n')


""" Estruturas de Decisão:
Operadores: [if, else, elif]
Python interpreta a identação da linha para continuar 
executando o bloco de código de condicinal
"""
print("#### Estruturas de Decisão ####")
prova1 = 8
prova2 = 9

media = float((prova1 + prova2) / 2)

print("Ifs simples:")
if media >= 6:
    print("Parabéns!")                          # executa esta parte do código apenas na condição True
    print("Aluno aprovado!")

if media < 6 and media >= 4:
    print("Você está de recuperação!")

if media <= 4:
    print("Você está reprovado")
print('\n')

# refazendo com if, elif e else
print("Usando If, elif e else:")
if media >= 6:                                  # início do condicional
    print("Parabéns!")
    print("Aluno aprovado!")
    print(f"Média final: {media}.")
elif media < 6 and media >= 4:                  # para blocos condicionais do meio
    print("Você está de recuperação!")
    print(f"Média final: {media}.")
elif media < 4:
    print("Você está reprovado.")
    print(f"Média final: {media}.")
else:                                           # para blocos condicionais do final
    print("Média calculada incorretamente!\nVerifique!")
    print(f"Média final: {media}.")
print('\n')

# If alinhados: 
print("If alinhado:")
if True:
    if 10 == 10:
        print("Estou dentro do '10 == 10'.")
    else:
        print("Estou fora do '10 == 10.")
    print("Faço parte do primeiro If.")
print('\n')


""" Estruturas de repetição:
Operadores: [while, for]
"""
print("#### Estruturas de Repetição ####")

print("Exemplo de While com iterador:")
i = 0                                           # iterador para auxiliar a validação da repetição
while i <= 10:
    print(f"{i:2}: Olá, estou dentro do While!")
    i += 1
print("Fim do While.")
print('\n')

print("Outro exemplo de While com iterador:")
i = 0
numero = int(input("Informe um número: "))
while i <= 10:
    print(f"{numero} X {i} = {numero * i}")
    i += 1
print('\n')

print("Exemplo de While com validação por input:")
nota = 0
while nota != -1:
    nota = float(input("Digite a nota de 1 aluno ou -1 para sair: "))
    if nota >= 6 and nota <= 10:
        print(f"Nota: {nota}. Aluno Aprovado!")
    elif nota < 6 and nota >= 4:
        print(f"Nota: {nota}. Aluno está em RECUPERAÇÃO!")
    elif nota < 4 and nota >= 0:
        print(f"Nota: {nota}. Aluno está REPROVADO!")
    else:
        if nota != -1:
            print("\nValor incorreto! Informe novamente!\n")
print('\n')

print("Exemplo de While com break:")
while True:
    nota = float(input("Digite a nota de 1 aluno ou -1 para sair: "))
    if nota >= 6 and nota <= 10:
        print(f"Nota: {nota}. Aluno Aprovado!")
    elif nota < 6 and nota >= 4:
        print(f"Nota: {nota}. Aluno está em RECUPERAÇÃO!")
    elif nota < 4 and nota >= 0:
        print(f"Nota: {nota}. Aluno está REPROVADO!")
    else:
        if nota != -1:
            print("\nValor incorreto! Informe novamente!\n")
        else:
            print("Saída selecionada.")
            break
print('\n')

print("Exemplo de For:")
# o range pode ser uma lista: [1, 2, 6, 'Tiago', 12]
for i in range(0, 10):                          # range(inicio, término(-1)
    print(i)
print('\n')

print("Outro exemplo de For:")
numero = int(input("Digite um número: "))
for i in range(0, 11, 1):                       # range(inicio, término(-1), passos)
    print(f"{numero} X {i} = {numero * i}")
print('\n')

print("Outro exemplo de For:")
for i in range(0, 1001):
    if i % 2 == 0:                              # validar se número é par
        print(i)
print('\n')


""" Estrutura de dados:
Tópicos: Listas e Dicionários
Listas: list = [ x, y, z]
    Operadores: list.append(value)
                list.pop()
Dicionários: dic = {x1:value1, x2:value2, x3:value3}
    Operadores: 
"""
print("#### Estruturas de Dados ####")
print("Listas: ")
notas_alunos = [10, 7, 8, 9, 10]                # criando uma lista
notas_alunos[0] = 3                             # definindo ou alterando valor de um índice

print(notas_alunos)                             # imprime toda a lista

notas_alunos.append(32)                         # inclui ao final um valor
notas_alunos.pop()                              # remove último valor da lista
print('\n')


print("Exemplo de criação de lista: ")
notas = []                                      # criando lista vazia
while True:
    nota_aluno = float(input("Digite a nota do aluno ou -1 para sair: "))
    if nota_aluno == -1:
        break
    elif nota_aluno >= 0 and nota_aluno <= 10:
        notas.append(nota_aluno)
    else:
        print("\nValor incorreto! Tente novamente!\n")

print(f"Notas informadas: {notas}")
print("\n")

soma = 0
qtde = 0
for i in notas:
    soma += i                                   # somando todas as notas informadas
    qtde += 1                                   # iterador manual para calcular o total de índices

print(f"Quantidade de índides por 'qtde': {qtde}.")
print(f"Quantidade de índices por len(notas): {len(notas)}.")
print("\n")

media = soma / qtde

print(f"Média das notas informadas: {media:.2f}")
print("\n")

print("Dicionários: ")
pessoa = {'nome':'Tiago', 'altura':164, 'idade':32}
print(f"Informando valor do dicionário: {pessoa['nome']}")
print("\n")


""" Funções:
Funções são apropriadas para reaproveitamento de código
as funções sempre começa com 'def' e precisam ser invocadas no código
"""
print("Exemplo de função:")

# def soma_numeros():                             # função simples que apenas executa um código
#     print("Função executada!")
# soma_numeros()                                  # invocação da função
# print("\n")

# print("Outro exemplo de função:")
# def soma_numeros2(numero1, numero2):            # função com passagem de parâmetros
#     soma = numero1 + numero2
#     print(soma)
# soma_numeros2(8, 9)
# print("\n")

# def soma_numeros3(numero1, numero2):
#     soma = numero1 + numero2
#     return soma                                 # return irá retornar o valor em memória

from funcoes import soma_numeros, soma_numeros2, soma_numeros3

soma_numeros()
soma1 = soma_numeros2(8, 9)
soma2 = soma_numeros3(11, 10)

print(f"Soma1 = {soma1} e Soma2 = {soma2}.")

print("\n")

""" Modularização:
Irá separar códigos em vários arquivos para facilitar
leitura, entendimento e manutenção
Operadores: from 'módulo' import 'função1', 'funcao2', 'funcao3'
"""
