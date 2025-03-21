# O qué variavel?
# Variavel é um espaço de memória que armazena um valor.
# Em Python, as variáveis são criadas no momento em que você as define.
# Para criar uma variável, você precisa atribuir um valor a ela.
#
# Como criar uma variável?
# nome_variavel = valor
#
# Exemplo:
# nome = "Lariane"
# print(nome)
# Entrada de dados
# Para receber uma mensagem do usuário, você pode usar a função input().
# A função input() sempre retorna uma string.
#
# Exemplo:
# saudacao = str(input("Qual é o teu nome? "))
#
# Saída de dados
# Para exibir uma mensagem no console, você pode usar a função print().
#
# Exemplo:
# print(f'Prazer em te conhecer {saudacao}')
#
# Tipos de dados
# Em Python, os tipos de dados mais comuns são:
# int (números inteiros)
# float (números decimais)
# str (strings)
# bool (booleanos)
# list (listas)
# tuple (tuplas)
# dict (dicionários)
# set (conjuntos)
#
# Exemplo:
# numero_inteiro = 10
# numero_decimal = 10.5
# texto = "Olá, mundo!"
# verdadeiro = True
# falso = False
# lista = [1, 2, 3, 4, 5]
# tupla = (1, 2, 3, 4, 5)
# dicionario = {"nome": "Lariane", "idade": 24}
# conjunto = {1, 2, 3, 4, 5}
# Operadores
# Em Python, os operadores mais comuns são:
# Aritméticos: +, -, *, /, %, **, //
# Comparação: ==, !=, >, <, >=, <=
# Lógicos: and, or, not
# Atribuição: =, +=, -=, *=, /=, %=, **=, //=
# Exemplo:
# soma = 10 + 5
# print(soma)
#
# subtracao = 10 - 5
# print(subtracao)
#
# multiplicacao = 10 * 5
# print(multiplicacao)
#
# divisao = 10 / 5
# print(divisao)
# divisao_inteira = 10 // 5
# print(divisao_inteira)
#
# resto = 10 % 5
# print(resto)
#
# potencia = 10 ** 5
# print(potencia)
#
# igualdade = 10 == 5
# print(igualdade)
#
# diferente = 10 != 5
# print(diferente)
#
# maior = 10 > 5
# print(maior)
#
# menor = 10 < 5

# print(menor)
#
# maior_ou_igual = 10 >= 5
# print(maior_ou_igual)
#
# menor_ou_igual = 10 <= 5
# print(menor_ou_igual)
#
# e_logico = True and False
# print(e_logico)
#
# ou_logico = True or False
# print(ou_logico)
#
# negacao = not True
# print(negacao)
#
# CONCATENAÇÃO
# Para concatenar strings em Python, você pode usar o operador +.
# Exemplo:
# nome = "Lariane"
# sobrenome = "Santos"
# nome_completo = nome + " " + sobrenome
# print(nome_completo)
#
# Para concatenar strings e números em Python, você precisa converter o número para string.
# Exemplo:
# numero = 10
# texto = "O número é " + str(numero)
# print(texto)
#
# Para concatenar strings e números em Python, você também pode usar a função format().
# Exemplo:
# numero = 10
# texto = "O número é {}".format(numero)
# print(texto)
#
# Para concatenar strings e números em Python, você também pode usar f-strings.
# Exemplo:
# numero = 10
# texto = f"O número é {numero}"
# print(texto)

# ESTRUTURAS CONDICIONAIS
# Em Python, as estruturas condicionais mais comuns são:
# if
# elif
# else
# Exemplo:
# numero = 10
# if numero > 0:
#     print("O número é positivo")
# elif numero < 0:
#     print("O número é negativo")
# else:
#     print("O número é zero")
#
# ESTRUTURAS DE REPETIÇÃO
# Em Python, as estruturas de repetição mais comuns são:
# for
# while
# Exemplo:
# for i in range(5):
#     print(i)
#
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#
# FUNÇÕES
# Em Python, você pode definir funções usando a palavra-chave def.
# Exemplo:
# def saudacao(nome):
#     print(f"Olá, {nome}!")
#
# saudacao("Lariane")
#
# Em Python, você pode definir funções com argumentos padrão.
# Exemplo:
# def saudacao(nome, saudacao="Olá"):
#     print(f"{saudacao}, {nome}!")
#
# saudacao("Lariane")
#
# Em Python, você pode definir funções que retornam valores.
# Exemplo:
# def soma(a, b):
#     return a + b
#
# resultado = soma(10, 5)
# print(resultado)
#
# Em Python, você pode definir funções com argumentos variáveis.
# Exemplo:
# def soma(*args):
#     resultado = 0
#     for arg in args:
#         resultado += arg
#     return resultado
#
# resultado = soma(1, 2, 3, 4, 5)
# print(resultado)
