#Declaracion de variables las cuales se usan como stock para este algoritmo
pc=30
mouse=80
keyboard=80
screen=30
total=0
product_list=[]
election=""
print("Bienvenido a Megatecnologia")
while True:
#Validacion sobre la elecion de seguir comprando, para hacer break en todos los while(Es una validacion util para la seccion de los productos)
    if election.lower()=="no":
            break
    if election=="":#Validacion para que este mensaje aparezca 1 sola vez en toda la ejecucion del algoritmo
        decsion=input("Desea comprar algun producto? SI/NO ")
#Validacion de la decision, determina si el programa sigue o termina
    if decsion.lower()=='no':
        print("Vuelva pronto")
        break
#Validacion para que se ingrese una opcion valida
    elif decsion.lower()!="si" and decsion.lower()!="no":
        print("la opcion ingresada no es valida")
        continue
    if decsion.lower()=="si": 
        print("Los productos que tenemos son:")
        product=int(input("1.pc($1800), 2.mouse($800),3.keyboar($600),4.screen($1000),5.Finalizar proceso. Elija un numero del producto que desee."))  
    #Inicio de la operacion del producto 1(pc)
        if product==1:
            while True:
                amount=int(input("Cuantas computadoras desea?(Ingrese 0 si cambio de opinion)"))
                #Valida la opcion 0 y termina el bucle y vuelve al bucle principal
                if amount==0:
                    print("Muchas gracias")
                    break
                #Valida una opcion valida
                elif amount<0:
                    print("Ingrese una opcion valida")
                    continue
                #Si la opcion es valida realizar la siguiente secuencia de intstrucciones
                else:
                    #Valida que la cantidad sea menor a la cantidad del producto disponible
                    if amount>pc:
                        print("Lo sentimo no hay stock")
                        break
                    #Si hay stock realizar las siguientes instrucciones
                    else:
                        #Calculos para cambiar la variable del stock y el total
                        total+=amount*1800
                        print(f"El precio a pagar es: {total}")
                        product_list.append("pc")#Añade el nombre del producto a la lista
                        #While necesario para pedir varias veces si la opcion es incorrecta
                        while True:
                            election=input("Desea seguir comprando?")
                            if election.lower()=="si" or election.lower()=="no":
                                break
                            else:
                                print("Selecione una opcion valida")
                        #Una vez finalizado el while si o si este bucle while se acaba, gracias a las siguientes instrucciones
                        if election.lower()=="si":
                            break
                        elif election.lower()=="no":
                                break
#Inicio de la operacion del producto 2(mouse)
        elif product==2:  
            while True:
                amount=int(input("Cuantos mouse desea?(Ingrese 0 si cambio de opinion)"))
                #Valida la opcion 0 y termina el bucle y vuelve al bucle principal
                if amount==0:
                    print("Muchas gracias")
                    break
                #Valida una opcion valida
                elif amount<0:
                    print("Ingrese una opcion valida")
                    continue
                #Si la opcion es valida realizar la siguiente secuencia de intstrucciones
                else:
                    #Valida que la cantidad sea menor a la cantidad del producto disponible
                    if amount>mouse:
                        print("Lo sentimos no hay stock")
                        break
                    #Si hay stock realizar las siguientes instrucciones
                    else:
                        #Calculos para cambiar la variable del stock y el total
                        mouse-=amount
                        total+=amount*800
                        print(f"El precio a pagar es: {total}")
                        product_list.append("mouse")#Añade el nombre del producto a la lista
                        #While necesario para pedir varias veces si la opcion es incorrecta
                        while True:
                            election=input("Desea seguir comprando?")
                            if election.lower()=="si" or election.lower()=="no":
                                break
                            else:
                                print("Selecione una opcion valida")
                        #Una vez finalizado el while si o si este bucle while se acaba, gracias a las siguientes instrucciones
                        if election.lower()=="si":
                                break
                        elif election.lower()=="no":
                                break
#Inicio de la operacion del producto 3(teclado)
        elif product==3:
            while True:
                amount=int(input("Cuantos teclados desea?(Ingrese 0 si cambio de opinion)"))#Pedir un dato y almacenar en la variable
                #Valida la opcion 0 y termina el bucle y vuelve al bucle principal
                if amount==0:
                    print("Muchas gracias")
                    break
                #Valida una opcion valida
                elif amount<0:
                    print("Ingrese una opcion valida")
                    continue
                #Si la opcion es valida realizar la siguiente secuencia de intstrucciones
                else:
                    #Valida que la cantidad sea menor a la cantidad del producto disponible
                    if amount>keyboard:
                        print("Lo sentimos no hay stock")
                        break
                    #Si hay stock realizar las siguientes instrucciones
                    else:   
                        #Calculos para cambiar la variable del stock y el total
                        keyboard-=amount
                        total+=amount*600
                        print(f"El precio a pagar es: {total}")
                        product_list.append("teclado")#Añade el nombre del producto a la lista
                        #While necesario para pedir varias veces si la opcion es incorrecta
                        while True:
                            election=input("Desea seguir comprando?")
                            if election.lower()=="si" or election.lower()=="no":
                                break
                            else:
                                print("Selecione una opcion valida")
                        #Una vez finalizado el while si o si este bucle while se acaba, gracias a las siguientes instrucciones
                        if election.lower()=="si":
                            break
                        elif election.lower()=="no":
                            break  
#Inicio de la operacion del producto 4(pantalla)   
        elif product==4:
            while True:
                amount=int(input("Cuantas pantallas desea?(Ingrese 0 si cambio de opinion)"))#Pedir un dato y almacenar en la variable
                #Valida la opcion 0 y termina el bucle y vuelve al bucle principal
                if amount==0:
                    print("Muchas gracias")
                    break
                #Valida una opcion valida
                elif amount<0:
                    print("Ingrese una opcion valida")
                    continue
                #Si la opcion es valida realizar la siguiente secuencia de intstrucciones
                else:
                    #Valida que la cantidad sea menor a la cantidad del producto disponible
                    if amount>screen:
                        print("Lo sentimos no hay stock")
                        break
                    #Si hay stock realizar las siguientes instrucciones
                    else:
                        #Calculos para cambiar la variable del stock y el total
                        screen-=amount
                        total+=amount*1000
                        print(f"El precio a pagar es: {total}")
                        product_list.append('pantalla')#Añade el nombre del producto a la lista
                        #While necesario para pedir varias veces si la opcion es incorrecta
                        while True:
                            election=input("Desea seguir comprando?")   
                            if election.lower()=="si" or election.lower()=="no":
                                break
                            else:
                                print("Selecione una opcion valida")
                        #Una vez finalizado el while si o si este bucle while se acaba, gracias a las siguientes instrucciones
                        if election.lower()=="si":
                            break
                        elif election.lower()=="no":
                                break
#Inicio de la operacion de la eleccion 5(Finalizar proceso)
        elif product==5:
            print("Vuelva pronto")
            break
#Validacion de una opcion invalida reinicia el bucle while
        else:
            print("Ingrese una opcion valida")  
            continue

if total>0:#Validacion para saber si el cliente compro algun producto 
    print(f"Muchas gracias por comprar en megatecnologia su total a pagar es: ${total}")
    product_list_non_repeated=set(product_list)#Pasar la lista en un set para que no se repitan valores
    print("Los productos comprados fueron:")
    for i in product_list_non_repeated:
        print(i)#Mostrar cada producto
print("Gracias por venir vuelva pronto")