#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ejercicio1
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import funciones
dni_number=int(input("Ingrese su N° de DNI"))
print(funciones.digits(dni_number))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ejercicio 2
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import funciones
phrase=input("Ingrese una frase de mas de 2 palabras")
print(funciones.last_word(phrase))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ejercicio 3
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import funciones
socios=[]
cant_socios=int(input('ingrese cantidad de socios: '))
for i in range(1,cant_socios+1):
    print(f'ingrese nombre del socio {i}')
    nombre=input('')
    while True:
        print(f'ingrese dni del socio {i}')
        dni=input('') 
        if len(dni)==7 or len(dni)==8:
            break 

    socios.append(funciones.id_unico(nombre,dni))
print('los id de los usuarios son: ')
print(socios)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ejercicio 4
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import funciones
num1=int(input("Ingrese un número"))
num2=int(input("Ingrese un número"))
if num1%num2==0 or num2%num1==0:
    print("Uno de los números ingresados es múltiplo del otro")
print(funciones.multi(num1,num2))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ejercicio 5
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import funciones
days=int(input("Ingrese la cantidad de días"))
if days==1:
    max_temp=int(input("Ingrese la temperatura máxima"))
    min_temp=int(input("Ingrese la temperatura mínima"))
    print(f"La temperatura media es ",(funciones.temperature(max_temp,min_temp)))
elif days>1:
    for i in range(days):
        max_temp=int(input("Ingrese la temperatura máxima"))
        min_temp=int(input("Ingrese la temperatura mínima"))
        print(f"La temperatura media es ",(funciones.temperature(max_temp,min_temp)))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ejercicio 6
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import funciones
phrase=input("Ingrese una frase o una palabra")
print(funciones.space(phrase))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ejercicio 7
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import funciones
number_ls=[]
end=int(input("Ingrese la cantidad de números que desea ingresar"))
for i in range(end):
    number=int(input("Ingrese number"))
    number_ls.append(number)
print(number_ls)
print(funciones.max_and_min(number_ls))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ejercicio 8
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import funciones
import math 
num=math.pi
radio=int(input("Ingrese el radio de una circunferencia "))
print("El area de la circunferencia es ",(funciones.area(num,radio)))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ejercicio 9
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import funciones

intentos=3

while True:
    user=input('ingrese usuario: ')
    password=input('ingrese contraseña: ')
    if funciones.login(user,password):
        print('felicitaciones, ingresaste')
        break
    else:
        intentos-=1 
    if intentos==3:
        print('has alcanzado el limite')
        break
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ejercicio 10
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import funciones
productos={
'producto1':24,
'producto2':50,
'producto3':100
}
descuentos={
'producto1':10,
'producto2':15,
}
precio_final = funciones.carrito(productos, descuentos)
print("Precio final con descuento:", precio_final)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ejercicio 11
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import funciones
lista=['hola','gente']
listaA=funciones.funcion(lista)
print(listaA)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ejercicio 12
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import funciones

cadena=input('ingrese una frase: ')
dicc=funciones.dicc(cadena)
print(dicc)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ejercicio 13
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import funciones

num1=float(input('ingrese primer numero del vector: '))
num2=float(input('ingrese el segundo numero del vector: '))
modulo=funciones.mod(num1,num2)
print(f'el modulo del vector con valores {num1} y {num2} es {modulo}')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ejercicio 14
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import funciones
num=int(input('ingrese un numero: '))
es_primo=funciones.es_primo(num)
print(es_primo)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ejercicio 15 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import funciones
fact=1
cont=0
while True:
    n=int(input('ingrese un numero, ingrese 0 para salir del programa: '))
    cont+=1
    funciones.factorial(fact,n)
    if n==0:
        break
print(f'se ingresaron {cont} numeros') 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ejercicio 16
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import funciones
num=int(input('ingrese un numero: '))
dig=int(input('ingrese un digito: '))
total=funciones.fre(num,dig)
print(f'el digito {dig} se encuentra {total} veces')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ejercicio 17
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import funciones
nummayor=0
fact=1
while True:
    num=int(input('ingrese un numero primo: '))
    if num>nummayor:
        nummayor=num
    if funciones.es_primo(num):
        sumadigit=0
        contf=0
        for i in str(num):
            sumadigit+=int(i)
        print(f'la suma de los digitos es: {sumadigit}')
        frec=int(input('ingrese un numero a buscar en el numero: '))
        for i in str(num):
            if str(frec)==i:
                contf+=1
        print(f'el numero {frec} se encuenta {contf} en el numero {num}')
                        
    if not funciones.es_primo(num):
        break
funciones.fact(fact,nummayor)    











