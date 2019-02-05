#!/usr/bin/python3

lista=range(1,11)
numeros=range(1,11)

for numero in lista:
    print("tabla del " + str(numero))
    print("------------")
    for value in numeros:
        print(str(numero) + " por " + str(value) + " es " + str(value*numero)+"  ")
    print("\n")
