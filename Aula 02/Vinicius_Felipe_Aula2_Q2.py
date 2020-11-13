
print ("------------------------------------------------")

valor = float(input("Qual o valor da prestação?: R$ "))
tempo = int(input("Quanto tempo de atraso?: "))
taxa = float(input("Quanto é a taxa?: "))

prestacao = valor+(valor*(taxa/100)*tempo)

print("\nO valor da prestação é: R$", prestacao)
 
print ("------------------------------------------------")