# -*- coding: utf-8 -*-



#4. Fa�a um Programa que leia os 3 lados de um tri�ngulo. O programa dever� informar se os valores podem 
#ser um tri�ngulo. Se sim, calcule e mostre a �rea do tri�ngulo.

a = float(input("Informe a base do triangulo: "))
b = float(input("Informe a altura do triangulo "))
c = float(input("Informe o terceiro lado do triangulo, o 2 lado do triangulo: "))

if (a + b <= c) or (a + c <= b) or (b + c <= a):   
    areaTriangulo = a * b / 2
    print("area do triangulo e: {0}" .format(areaTriangulo))
else: 
    print("Os valores informados nao formam um triangulo")
