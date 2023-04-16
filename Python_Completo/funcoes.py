def soma_numeros():                             # função simples que apenas executa um código
    print("Função executada!")
soma_numeros()                                  # invocação da função
print("\n")

print("Outro exemplo de função:")
def soma_numeros2(numero1, numero2):            # função com passagem de parâmetros
    soma = numero1 + numero2
    print(soma)
soma_numeros2(8, 9)
print("\n")

def soma_numeros3(numero1, numero2):
    soma = numero1 + numero2
    return soma                                 # return irá retornar o valor em memória

