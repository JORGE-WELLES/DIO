
def calculadoram(num1, num2, oper):
    if oper == 1:
        resultado = num1 + num2
    elif oper == 2 :
        resultado = num1 - num2
    elif oper == 3 :
        resultado = num1 * num2
    elif oper == 4 :
        resultado = num1 / num2
    return resultado

calculo = calculadoram(10, 2, 4)
print(calculo)
