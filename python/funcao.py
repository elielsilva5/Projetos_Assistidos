# FUNÇÕES

# 1. O que são funções e por que utiliza-las

# Funções que já utilizamos anteriormente...

'''print() # imprime uma mensagem (int, float, str) no console (terminal, CMD)
input() # retorna um dado informado pelo usuario (entrada padrão) e pode receber uma string 
len() # recebe uma lista e reotrna o tamanho dessa lista
# max() # retorna o maior valor de uma lista'''

# 2. Criação de função

# função inicial

def saudacao():
    print('Seja bem vindo!')

    print( 'Olá, é um prazer ter você conosco!' )
saudacao()
saudacao()
saudacao()

# função com parâmetros

def saudacao(nome, curso):

    print(f'Seja bem vindo(a), {nome}!')

    print( f'É um prazer ter você conosco no curso de {curso}!' )

saudacao('Eliel', 'Python')

# Função com parâmetros default

def saudacao(nome, curso = 'Python'):

    print(f'Seja bem vindo(a), {nome}!')

    print( f'É um prazer ter você conosco no curso de {curso}!' )

saudacao('Eliel')

# Funções com retorno

def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)

print('O resultado da soma é:', resultado)

def calculadora(num1, num2, operacao = '+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2

resultado = calculadora(10, 20, '-')

print(resultado)