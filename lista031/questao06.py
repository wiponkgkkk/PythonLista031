#6) Fazer um programa que pergunte uma temperatura ao usuário, em graus Fahrenheit, e apresente esta
#temperatura convertida em graus Celsius. A fórmula da conversão é c	=	(f	–	32)	x	5	:	9	, onde c	 é a temperatura
#em graus Celsius e f		em Fahrenheit

#Input

fah = float(input("Informe o valor de uma temperatura em Graus Fahrenheit " ))

#Prints

print("O valor da temperatura em Graus Celsius é %.2f " %((fah - 32) * 5 / 9))