print("----------------------------calculadora em python-------------------------------")
print("")
print("Selecione a operação desejada")
print("")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")


def soma():
        numsoma1 = int(input("primeiro numero: "))
        numsoma2 = int(input("segundo numero: "))
        adição = numsoma1 + numsoma2
        print("Resultado: %s " %(adição))
        return adição
        
        
def subtração():
        numsubtrair1 = int(input("primeiro numero: "))
        numsubtrair2 = int(input("segundo numero: "))
        subtrair = numsubtrair1 - numsubtrair2
        print("Resultado: %s " %(subtrair))
        return subtrair

def multiplicação():
       numultiplicar1 = int(input("primeiro numero: "))
       numultiplicar2 = int(input("segundo numero: "))  
       multiplicar = numultiplicar1 * numultiplicar2
       print("Resultado: %s " %(multiplicar))
       return multiplicar

def divisão():
       numdividir1 = int(input("primeiro numero: "))       
       numdividir2 = int(input("segundo numero: "))
       dividir = numdividir1 / numdividir2
       print("Resultado: %s " %(dividir))
       return dividir




opção = int(input("Digite o numero refente a opção: "))
print("")
listaop = [1,2,3,4]



for i in listaop:

    if opção == listaop[0]:
         soma()
         opc = int(input("Deseja continuar a operação? digite 1-continuar, 2-voltar ao menu, 3-encerrar:  "))
         print("")
         if opc == 1:
           continue
         elif opc == 2:
           opção = int(input("Digite o numero refente a operação (1-soma/2-subtração/3-multiplicação/4-divisão): "))
           print("")
         elif opc == 3:
           break 
         elif opc > 3:
           opc = int(input("Deseja continuar a operação? digite 1-continuar, 2-voltar ao menu, 3-encerrar:  "))
           print("")
         

    elif opção == listaop[1]:
        subtração()
        opc = int(input("Deseja continuar a operação? digite 1-continuar, 2-voltar ao menu, 3-encerrar:  "))
        print("")
        if opc == 1:
           continue
        elif opc == 2:
           opção = int(input("Digite o numero refente a operação (1-soma/2-subtração/3-multiplicação/4-divisão): "))
           print("")
        elif opc == 3:
           break 
        elif opc > 3:
           opc = int(input("Deseja continuar a operação? digite 1-continuar, 2-voltar ao menu, 3-encerrar:  "))
           print("")


    elif opção == listaop[2]:
        multiplicação()
        opc = int(input("Deseja continuar a operação? digite 1-continuar, 2-voltar ao menu, 3-encerrar:  "))
        print("")
        if opc == 1:
           continue
        elif opc == 2:
           opção = int(input("Digite o numero refente a operação (1-soma/2-subtração/3-multiplicação/4-divisão): "))
           print("")
        elif opc == 3:
           break 
        elif opc > 3:
           opc = int(input("Deseja continuar a operação? digite 1-continuar, 2-voltar ao menu, 3-encerrar:  "))
           


    elif opção == listaop[3]:
        divisão()
        opc = int(input("Deseja continuar a operação? digite 1-continuar, 2-voltar ao menu, 3-encerrar:  "))
        print("")
        if opc == 1:
           continue
        elif opc == 2:
           opção = int(input("Digite o numero refente a operação (1-soma/2-subtração/3-multiplicação/4-divisão): "))
           print("")
        elif opc == 3:
           break 
        elif opc > 3:
           opc = int(input("Deseja continuar a operação? digite 1-continuar, 2-voltar ao menu, 3-encerrar:  "))
           print("")
    else:
     opção = int(input("Opção incorreta! Digite o numero refente a opção: "))
     print("")





