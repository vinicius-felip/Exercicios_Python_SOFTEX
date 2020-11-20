print('-------------Digite dois números--------------')
num = int(input("Número 1: "))
num2 = int(input("Número 2: "))

print('----------------------------------------------')

print("Divisor: ", num)

if num2 == 0:
    print("Dividendo: 0 não pode ser o dividendo")
else:
    print("Dividendo: ", num2)
    
if num2 == 0:
    print("Quociente: 0 não pode ser o dividendo")
else:
    print("Quociente: ", num/num2)

if num2 == 0:
    print("Resto: 0 não pode ser o dividendo")
else:
    print("Resto: ", num%num2)

print('----------------------------------------------')

