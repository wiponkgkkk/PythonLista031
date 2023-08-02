#8) Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem. O
#programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros; qual é o
#valor do consumo médio do automóvel, em quilômetros por litro

#Inputs

dist = int(input("Qual a distancia percorrida na viagem em Km ? " ))
cm = int(input("Qual valor médio do consumo do automovel em quilômetros por litro ? " ))

#Cálculos

vt = dist // cm

#Prints

print(f" Você gastará {vt} litros de combustível em sua viagem")