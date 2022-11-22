def add(x, y): 
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def checkid(id):
    if id in ('1', '2', '3', '4'):
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

def calcgeral(id, num1, num2,continue):
    
    if checkid(id) == 1:

        if id == '1':
            return add(num1, num2)

        elif id == '2':
            return subtract(num1, num2)

        elif id == '3':
            return multiply(num1, num2)

        elif id == '4':
            return divide(num1, num2)
        
        if continuecalc(continue) == 0 or continuecalc(continue) == -1:
          break
    
    else:
        print("Id nao reconhecido")