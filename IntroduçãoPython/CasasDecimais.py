# -*- coding: utf-8 -*-



#4. Faça um Programa que leia os 3 lados de um triângulo. O programa deverá informar se os valores podem 
#ser um triângulo. Se sim, calcule e mostre a área do triângulo.

a = float(input("Informe a base do triângulo: "))
b = float(input("Informe a altura do triangulo "))
c = float(input("Informe o terceiro lado do triangulo, o 2 lado do triangulo: "))

if (a + b <= c) or (a + c <= b) or (b + c <= a):   
    areaTriangulo = a * b / 2
    print("area do triangulo e: {0}" .format(areaTriangulo))
else: 
    print("Os valores informados nao formam um triangulo")
