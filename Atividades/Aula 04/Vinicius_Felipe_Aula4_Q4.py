import os

nome = []
notas = []
nota = []
media  = []
alunos = dict(Nome = nome, Notas = notas, Media = media)
os.system('cls')
compr = int(input('Quantos alunos você deseja cadastrar? '))
os.system('cls')
for i in range(compr):
    nota = []
    nome.append(input('Qual o nome do aluno? '))
    nota.append(float(input('Qual a primeira nota do aluno? ')))
    nota.append(float(input('Qual a segunda  nota do aluno? ')))
    notas.append(nota)
    media.append(sum(notas[i])/2)
    os.system('cls')
    

print("No.  NOME            MÉDIA") 
print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")    
for i in range(compr):  
    print(f"{i+1:<4} {alunos['Nome'][i]:<16} {alunos['Media'][i]:.2f}")

print("___________________________\n")    

loop = True
while loop == True:
    opc = int(input('Deseja saber as nota de qual aluno? (Digite o número do aluno (0 = Finalizar)): '))
    if not opc in range(compr+1):
        print("Aluno não encontrado")
    
    elif opc != 0:       
        print("___________________________\n")
        print(f"Notas de {alunos['Nome'][i]} são {alunos['Notas'][opc-1]}")
        print("___________________________\n")   
    else:
        loop = False
        print ("Volte sempre")

