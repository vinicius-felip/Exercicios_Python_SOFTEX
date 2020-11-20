
print ("---------------------------------------------------")
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))
freq = float(input("Digite sua taxa de frequência: "))

def mediaAritmetic (a,b,c):  
    media = ((a+b+c)/3)
    return media

media = mediaAritmetic(nota1,nota2,nota3)

print ("---------------------------------------------------")

if freq>=75:
    if media>7:
        print ("Você foi aprovado com média: ", media)
    else:
        print ("Você foi reprovado com média: ", media)
else:
    print ("Você foi reprovado por falta")
print ("---------------------------------------------------")
