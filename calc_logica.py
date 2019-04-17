# https://notebooks.azure.com/ViniciusPereira/libraries/truth-table

from itertools import product

import string

#Função que retorna chamada para tabela
#E recebe o array correspondente a expressão inserida
def variaveis(p, n = 1):
    #O parametro n = 1 é usado como classificador
    #se for == 1 retorna a tabela
    #se for diferente de 1 retorna a quantidade de variaveis
    #Sinais são as representações dos operadores
    sinais = ['~','@','^']
    var = []
    for i in p:
        if i not in sinais:    
            #Cria um array apenas com letras
            var.append(i)
    if n == 1:
        return tabela(var)
    else:
        return var

#Função que retorna chamada para tabela
#E recebe o array correspondente as letras da expressão
def tabela(p):
    qtd_arg = len(p)
    #A quantidade de letras é utilizado como parametro para a função product
    table = product(range(2), repeat = qtd_arg)
    #Retorna a tabela verdade
    return table

#Função que retorna expressão final
#E recebe o array correspondente ao array da expressão
def operacao(p):
    operacao_completa = []
    #Ao reconhecer um item acrescenta um valor ao array
    for i in p:
        if i == '^':
            operacao_completa.append(" and ")
        elif i == '@':
            operacao_completa.append(" or ")
        elif i == '(':
            operacao_completa.append("(") 
        elif i == ')':
            operacao_completa.append(")")
        elif i in list(string.ascii_letters):
            operacao_completa.append(i)     
        elif i == '~':
            operacao_completa.append(" not ")
    #Retorna array com a expressão completa
    return operacao_completa

#As funções z convertem a expressão completa para código e as retornam
#Existem 3 para 3 tipos de senários possiveis
def zz(a, b):    
    luk = ''.join(str(e) for e in operacao(ll))
    return eval(luk)


def zzz(a, b, c):    
    luk = ''.join(str(e) for e in operacao(ll))
    return eval(luk)

def zzzz(a, b, c, d):    
    luk = ''.join(str(e) for e in operacao(ll))
    return eval(luk)

def run(tabela):
    #Identifica qual função z utilizar
    for i in tabela:
        if len(variaveis(ll, n = 2)) == 2:
            print(i, zz(*i))
        elif len(variaveis(ll, n = 2)) == 3:
            print(i, zzz(*i))
        elif len(variaveis(ll, n = 2)) == 4:
            print(i, zzzz(*i))

while True:
    print("ESSE PROGRAMA EXECUTA A O CALCULO DE TABELA VERDADE")
    print("AS VARIAVES POSSIVEIS SÃO A, B, C, D")
    print("AS OPERAÇÕES POSSIVEIS SÃO @ = OU e ^ = E")

    #Recebe expressão
    l = input()
    #Converte expressão para vetor
    ll = l.split()
    #executa o código
    run(variaveis(ll))
    print("\n---------------------------\n\n")

