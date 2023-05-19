from time import sleep

def soma(num, num2):
    res = num + num2
    return res

def subtração(num, num2):
    res = num - num2
    return res
def multiplicação(num,num2):
    res =  num * num2
    return res
def divisão(num,num2):
    res = num / num2
    return res

def resto(num,num2):
    res = num % num2
    return res

def exponecial(num, num2):
    res = num ** num2
    return res

def imparoupar(num):
    if num %2 == 0:
        res = "par"
    else: 
        res = "impar"
    
    return res




print(50*"=")
print("Bem vindo ao programa calculadora")
print(50*"=")

nome = input("Digite o seu nome: ")
print("\nInicializando calculadora")
sleep(5)

print(f"\nCalculadora inicializada. Olá {nome}, vamos começar a resolver 'enigmas'?")
 

continuar = "s"
while(continuar == "s" or continuar == "sim" or continuar == "Sim" or continuar == "S"):    
    try:
        conta = input("\nDigite o operador logico (Soma, Subtração, Multiplicação, Divisão, Exponenciação, Resto de Divisão ou Impar ou Par ) ")
    except:
        print("\nVoce deve escolher algumas das opções")
    
            
    if(conta == "Soma" or conta == "soma"):
        try:
            num = float(input("\nDigite o primeiro numero:  "))
            num2 = float(input("\nDigite o segundo numero:  "))
            print(f"o resultado da soma é {soma(num,num2)}")
        except ValueError:
            print("\nVocê deve digitar somente numero, não letras ou simbolos")


    elif(conta == "Subtração" or conta == "subtração"):
        try:
            num = float(input("\nDigite o primeiro numero:  "))
            num2 = float(input("\nDigite o segundo numero:  "))
            print(f"o resultado da subtração é {subtração(num,num2)}")
        except ValueError:    
            print("\nVocê deve digitar somente numero, não letras ou simbolos")
        

    elif(conta == "Multiplicação" or conta == "multiplicação"):
        try:
            num = float(input("\nDigite o primeiro numero:  "))
            num2 = float(input("\nDigite o segundo numero:  "))
            print(f"o resultado da multiplicação é {multiplicação(num,num2)}")
        except ValueError:    
            print("\nVocê deve digitar somente numero, não letras ou simbolos")


    elif(conta == "Divisão" or conta == "divisão"):
        try:
             num = float(input("\nDigite o primeiro numero:  "))
             num2 = float(input("\nDigite o segundo numero:  "))
           
             print(f"\nO resultado da divisão dos numeros é {divisão(num, num2)}")
        except ValueError: 
            print("\nVocê deve digitar somente numero, não letras ou simbolos")
        except ZeroDivisionError:
            print("\nImpossivel dividir um numero por zero, tente novamente")

    elif(conta == "Exponenciação" or conta == "exponenciação"):
        try:
            num = float(input("\nDigite o primeiro numero:  "))
            num2 = float(input("\nDigite o segundo numero:  "))
            print(f"\nO resultado da exponenciação é {exponecial(num, num2)}")

        except ValueError:
            print("\nVocê deve digitar somente numero, não letras ou simbolos")

        

    elif(conta == "Resto de Divisão" or conta == "resto de divisão"):
        try:
            num = float(input("\nDigite o primeiro numero:  "))
            num2 = float(input("\nDigite o segundo numero:  "))
            print(f"\nO resto da divisão é {resto(num, num2)}")

        except ValueError:
            print("\nVocê deve digitar somente numero, não letras ou simbolos")
        except ZeroDivisionError:
            print("\nImpossivel dividir um numero por zero, tente novamente")

        


    elif(conta == "Impar ou Par" or conta == "impar ou par"):
        try:
            num = int(input("\nDigite o primeiro numero:  "))
            print(f"\nO numero é {imparoupar(num)}")
        except ValueError: 
            print("\nVocê deve digitar somente numero, não letras ou simbolos")
    sleep(4)   
    continuar = input("\nVoce deseja fazer outra operação (s/n)? ")
