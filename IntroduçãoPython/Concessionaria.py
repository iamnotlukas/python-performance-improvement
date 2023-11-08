
#2. Uma revendedora de carros usados paga a seus funcionários 
#vendedores um salário fixo por mês, mais uma comissão também fixa para 
#cada carro vendido e mais 5% do valor das vendas por ele efetuadas.
# Escrever um algoritmo que leia o número de carros por ele vendidos, 
# o valor total de suas vendas, o salário fixo e o valor que ele recebe 
# por carro vendido. Calcule e escreva o salário final do vendedor. 


salarioFixo = int(input("Informe o salario fixo do funcionario: "))
numeroDeCarrosVendidos = int(input("Informe o numero de carros vendidos pelo vendedor: "))
valorVendas = int(input("Informe o valor total das vendas: "))

comissaoPorCarro = 0.05 * valorVendas
comissaoTotal = comissaoPorCarro + numeroDeCarrosVendidos 
salarioFinal  = salarioFixo + comissaoTotal  

print("O salario do vendedor e de: {0} " .format(salarioFinal))
