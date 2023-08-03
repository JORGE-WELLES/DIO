def calculadora(num1, num2, op):
    
    
        if op == 1:
            resp = num1 + num2
            opera = " + "
            return print(str(num1) + opera + str(num2) + " = " + str(resp))
            
        elif op == 2:
                
                resp = num1 - num2
                opera = " - "
                return print(str(num1) + opera + str(num2) + " = " + str(resp))
        elif op == 3:
                
                resp = num1 * num2
                opera = " X "
                return print(str(num1) + opera + str(num2) + " = " + str(resp))
        elif op == 4:
                
                resp = num1 / num2
                opera = " ÷ "
                return print(str(num1) + opera + str(num2) + " = " + str(resp))
        
               
       

print("""
Escolha uma Opção:
           1 = Soma
           2 = Subtração
           3 = Multiplicação
           4 = Divisão
           0 = Sair
      
 """)



op = int(input("Escolha uma Opção: "))
if op != 0:
   num1 = int(input("Qual o primeiro valor "))
   num2 = int(input("Qual o segundo valor "))

while op != 0:
       calculadora(num1, num2, op)

       op = int(input("Escolha uma Opção: "))
       if op != 0:
          num1 = int(input("Qual o primeiro valor "))
          num2 = int(input("Qual o segundo valor "))
       


