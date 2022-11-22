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

def calcgeral(id, num1, num2, cont):
    
    if checkid(id) == 1:

        if id == '1':
            return add(num1, num2)

        elif id == '2':
            return subtract(num1, num2)

        elif id == '3':
            return multiply(num1, num2)

        elif id == '4':
            return divide(num1, num2)
        
        if continuecalc(cont) == 0 or continuecalc(cont) == -1:
          break
    
    else:
        print("Id nao reconhecido")