def numPrimo(num):
    if num== 1:
        print(f"{num} não é primo")
    if num== 2:
        print(f"{num} é primo")
    cont=0
    for x in range(2, num+1):
        if num % x == 0:
            cont+=1
    if cont > 1:
        print(f"{num} não é primo")

    else:
        print(f"{num} é primo")

def numUnicos(l):
    nova_lista=[]
    for x in l:
        if x not in nova_lista:
            nova_lista.append(x)
    print(nova_lista)


def argumento(texto):
    espa=0
    let=0
    for i in range (len(texto)):
        if texto[i] in ".,!? ":
            espa = espa + 1
            let = len(texto) - espa
    print(texto[::-1], end= "")
    print(f" é seu texto ao contrário e sua contagem de letras é {let}")

def somar(*numeros):
    soma=0
    for x in range(len(numeros)):
        soma+= numeros[x]
    print(soma)

def soma(x, y):
    soma=x+y
    print(soma)

def cadastro(nomes, senhas):
    nomes=["","","","",""]
    senhas=["","","","",""]

    for x in range(5):
        nomes[x]=input("digite seu nome: ")
        senhas[x]=input("digite sua senha: ")

def cottage(texto):
    cont=0
    conta=0
    cal=0
    for i in range (len(texto)):
        if texto[i]==" ":
            cont= cont + 1
            cal= len(texto)-cont
        elif texto[i] in "aeiouAEIOU":
            conta= conta +1
    print(f"seu texto tem {cal} letras, {cont} espaços e {conta} vogais")

def piramideDaBabilonia(numero):
    for x in range(1,numero+1):
        for y in range(1,x+1,1):
            print(y, end=" ")
        print()

def piramideDoEgito(numero):
    for x in range(1,numero+1):
        for y in range(1,x+1,1):
            print(x, end=" ")
        print()

def imprime_nome(nome):
    print(f"Nome: {nome}")
