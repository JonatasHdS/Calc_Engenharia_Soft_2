def add(x, y): 
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def checkid(choice):
    if choice in ('1', '2', '3', '4'):
        return 1
    else:
        return 0

def continuecalc(respost):
    if respost == "nao":
        return 0
    elif respost == "sim":
        return 1
    else:
        return -1

print("Selecione uma operacao.")
print("1.Soma")
print("2.Subtração")
print("3.Multiplicação")
print("4.Dividir")

while True:
    try:
        choice = input("Escolha entre (1/2/3/4): ")
    except EOFError as e:
        print(e)

    if checkid(choice) == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(add(num1, num2))

        elif choice == '2':
            print(subtract(num1, num2))

        elif choice == '3':
            print(multiply(num1, num2))

        elif choice == '4':
            print(divide(num1, num2))
        
        next_calculation = input("Continuar? (sim/nao): ")
        if continuecalc(next_calculation) == 0 or continuecalc(next_calculation) == -1:
          break
    
    else:
        print("Id nao reconhecido")