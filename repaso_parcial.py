pc=30
mouse=80
keyboard=80
screen=30
total=0
product_list=[]
election=""
print("Bienvenido a Megatecnologia")
while True:
#Validacion sobre la elecion de seguir comprando, para hacer break en todos los while
    if election.lower()=="no":
            break
    if election=="":
        decsion=input("Desea comprar algun producto? SI/NO ")
#Validacion de la decision, determina si el programa sigue o termina
   
    if decsion.lower()=='no':
        print("Vuelva pronto")
        break
    elif decsion.lower()!="si":
        print("la opcion ingresada no es valida")
        continue

    if decsion.lower()=="si":
       
        print("Los productos que tenemos son:")
        product=int(input("1.pc($1800), 2.mouse($800),3.keyboar($600),4.screen($1000),5.Finalizar proceso. Elija un numero del producto que desee."))  
    #Inicio de la operacion del producto 1(pc)
        if product==1:
            while True:
                amount=int(input("Cuantas computadoras desea?(Ingrese 0 si cambio de opinion)"))
                if amount==0:
                    print("Muchas gracias")
                    break
                elif amount<0:
                    print("Ingrese una opcion valida")
                    continue
                else:
                    if amount>pc:
                         print("Lo sentimo no hay stock")
                         break
                    else:
                        total+=amount*1800
                        print(f"El precio a pagar es: {total}")
                        product_list.append("pc")
                        while True:
                            election=input("Desea seguir comprando?")
                            if election.lower()=="si" or election.lower()=="no":
                                break
                            else:
                                print("Selecione una opcion valida")
                        
                        if election.lower()=="si":
                             break
                        elif election.lower()=="no":
                                break

        elif product==2:  
             while True:
                amount=int(input("Cuantos mouse desea?(Ingrese 0 si cambio de opinion)"))
                if amount==0:
                    print("Muchas gracias")
                    break
                elif amount<0:
                    print("Ingrese una opcion valida")
                    continue
                else:
                    mouse-=amount
                    total+=amount*800
                    print(f"El precio a pagar es: {total}")
                    product_list.append("mouse")
                    while True:
                        election=input("Desea seguir comprando?")
                        if election.lower()=="si" or election.lower()=="no":
                            break
                        else:
                            print("Selecione una opcion valida")
                        
                    if election.lower()=="si":
                            break
                    elif election.lower()=="no":
                            break
        elif product==3:
             while True:
                amount=int(input("Cuantos teclados desea?(Ingrese 0 si cambio de opinion)"))
                if amount==0:
                    print("Muchas gracias")
                    break
                elif amount<0:
                    print("Ingrese una opcion valida")
                    continue
                else:
                    if amount>keyboard:
                         print("Lo sentimos no hay stock")
                         break
                    
                    else:   
                        keyboard-=amount
                        total+=amount*600
                        print(f"El precio a pagar es: {total}")
                        product_list.append("teclado")
                        while True:
                            election=input("Desea seguir comprando?")
                            if election.lower()=="si" or election.lower()=="no":
                                break
                            else:
                                print("Selecione una opcion valida")
                        
                        if election.lower()=="si":
                            break
                        elif election.lower()=="no":
                            break     
        elif product==4:
             while True:
                amount=int(input("Cuantas pantallas desea?(Ingrese 0 si cambio de opinion)"))
                if amount==0:
                    print("Muchas gracias")
                    break
                elif amount<0:
                    print("Ingrese una opcion valida")
                    continue
                else:
                    if amount>screen:
                         print("Lo sentimos no hay stock")
                         break
                    else:
                        screen-=amount
                        total+=amount*1000
                        print(f"El precio a pagar es: {total}")
                        product_list.append('pantalla')
                        while True:
                            election=input("Desea seguir comprando?")   
                            if election.lower()=="si" or election.lower()=="no":
                                break
                            else:
                                print("Selecione una opcion valida")
                        
                        if election.lower()=="si":
                            break
                        elif election.lower()=="no":
                                break
        elif product==5:
             print("Vuelva pronto")
             break
        else:
             print("Ingrese una opcion valida")  
             continue



 

 

    





    