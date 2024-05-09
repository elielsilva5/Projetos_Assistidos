# Lisas

# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# com listas

notas = [7.9, 9.7, 8.2]

# Criando listas

lista = []
lista = list()
lista =[]
lista_de_listas = [10, [1, 2,3]]

# indexação e Slices (fatiamento)

lista = [10, 'Eliel', 3.14159, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

# Slices

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:2])

# Iterações com for

# 1. utilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)


# 2. utilizando indices

print('Comprimento da lista', len(lista))

for i in range(len(lista)):
    print(i)


# > MÉTODOS DE LISTAS

lista = [1, 3, 12, 8, 2]

# APPEND (adiciona o elemento no final)

print('antes do append', lista)

lista.append(3)

print('depois do apprnd', lista)


# INSERT (adiciona o elemento em uma posição escolhida)

lista.insert(2, 10)

print('depois do inseert', lista)

# extend (juntar duas listas)

lista2 = [1, 2, 3]

lista.extend(lista2)

print('depois do extend', lista)

# POP (remover um elemento, se não especificar, será removido o ultimo elemento)

lista.pop()

print('depois do pop', lista)


lista.pop(0)

print('depois do pop', lista)

# REMOVE (seleciona o valor do elemento a ser retirado)

lista.remove(3)

print('depois do remove', lista)

# COUNT (contar quantos elementos tem na lista)

print('quantidade de 2 na lista', lista.count(2))

# INDEX (mostra qual indice um determinado elemento dentro da lista* )

print('indice do elemento 12', lista.index(12))

#  SORT (ordenar a lista de forma crescente)

lista.sort(reverse=True)

print(lista)

# FUNÇÕES PARA LISTAS

# LEN (quantidade de elementos da lista)

print(len(lista))


#SUM (soma de lista)

print(sum(lista))


# MAX (reporta o maior valor da lista)

print('maior elemnto da lista:', max(lista))

# MIN (reporta o menor valor da lista)

print('menor elemnto da lista:', min(lista))





