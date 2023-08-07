#10) Fazer um algoritmo que efetue o cálculo do valor de uma prestação em atraso, utilizando a fórmula prestação	=
#valor	+	(valor	x	(taxa	:	100)	x	tempo	em	dias

#Inputs

val = float(input("Qual valor da prestação ? " ))
taxa = float(input("Qual valor da taxa de juros ? " ))
atrs = int(input("Quantos dias está atrasada ? " ))

#Prints

print(f"O valor após {atrs} dias de atraso será R$%.2f " %(val + (val *(taxa / 100) * atrs)))