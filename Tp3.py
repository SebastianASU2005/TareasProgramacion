# 1-Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
name = input("ingrese una palabra: ")
for p in range(11):
    print(name)
# 2-Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
age = int(input("ingresa tu edad: "))
for i in range(1, age):
    print(i)

# 3-Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
number = int(input("ingrese un numero"))
for i in range(1, number + 1):
    if i % 2 != 0:
        print(f"{i},")
# 4-Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

number = int(input("type number integer: "))
for p in range(number, -1, -1):
    print(f"{p},")

# 5-Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.


cashInverted = float(input("cuanta plata vas a invertir: "))
interestAnual = float(input("cuanto interes anual? "))
ages = int(input("por cuantos años el plazo fijo: "))
interestAnual = interestAnual / 100
for p in range(1, ages):
    cashInverted += cashInverted * interestAnual
    print(f"capital obtenido {cashInverted}")

# 6-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
hight = int(input("ingrese altura: "))
for i in range(1, hight + 1):
    print("*" * i)

# 7-Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.

for i in range(1):
    print("tabla del 1")
    for j in range(1, 10):
        print(f"{i} x {j} es : {i*j}")
#8)Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
num=int(input("Ingrese un numero"))
for i in range(1,num+1,2):
    for j in range(1,i+1,2):
     print(j,end=" ")
    print(" ")

#9)Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
password="Hola32"
answer=""
while answer!=password:
   answer=input("Ingrese la contraseña")
   if(answer!=password):
      print("Error contraseña incorrecta")
print("contraseña correcta")
#10)Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
numero = int(input("Ingrese un número entero positivo: "))
if numero <= 1:
        print("El número no es primo.")
else:
    es_primo = True
    for i in range(2, numero):
            if numero % i == 0:
                es_primo = False
                break
if es_primo:
 print(f"{numero} es un número primo.")
else:
 print(f"{numero} no es un número primo.")
 #11)Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
 word=(input("ingrese una palabra"))
 long=len(word)
 for i in range(long-1,-1,-1):
     letter=word[i]
     print(letter)
#12)Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
phrase=input("Ingrese una frase")
letter=input("Ingrese la letra que desea saber cuantas veces se repite en la frase")
cont=phrase.count(letter)
print(f"En la frase aparece la letra {letter}:aparece {cont} veces")
#13)Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
while True:
    eco = input("Ingrese una palabra, escriba 'salir' para terminar: ")
    if eco == "salir":
        break
    print(eco)
#14)Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.
start = int(input("Ingrese el primer número entero: "))
final = int(input("Ingrese el segundo número entero: "))

if start > final:
    start, final = final, start

print(f"Números pares entre {start} y {final}:")
for num in range(start, final + 1):
    if num % 2 == 0:
        print(num)

print(f"Números impares entre {start} y {final}:")
for num in range(start, final + 1):
    if num % 2 != 0:
        print(num)
#15)Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.
num = int(input("Ingrese un número entero mayor que cero: "))

print(f"Divisores de {num}:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
#16)escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.
amount=int(input("Cuantos numero va a ingresar"))
amountNegative=0
for i in range(1,amount+1):
    num=int(input(f"Ingrese el numero {i} "))
    if num<0:
        amountNegative+=1
print(f"La cantidad de numero negativos introducidos fue: {amountNegative}")
#17)Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).
phrase = input("Ingrese una frase: ").lower()  

vocals = "aeiou"
vocals_found = []

for letter in phrase:
    if letter in vocals and letter not in vocals_found:
        vocals_found.append(letter)

print("Vocales encontradas en la frase:")
for vocal in vocals_found:
    print(vocal)
#18)rear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
a= 0
b=1
print("Los primeros 10 números de la sucesión de Fibonacci son:")
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b
#19)Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar. 
# A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. 
# El programa deberá comprobar que las cantidades ingresadas sean positivas.
amount=int(input("Cuanto dinero desea ahorrar"))
saving=0
while saving<amount:
    money=int(input("Ingrese dinero" ))
    if money>=0:
        saving+=money
    else:
        print("No intruduzca numero negativos")
print(f"usted a ahorrado la cantidad deseada tiene {saving}")
#20)eer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
num=2
total=0
while num!=0:
    num=int(input("Ingrese un numero,ingrese 0 para salir del bucle"))
    total+=num
print(f"La suma de todos los numero ingresados es igual a: {total}")
#21)Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
num=2
max=0
while num!=0:
    num=int(input("ingrese un numero,ingrese 0 para salir del bucle"))
    if num>max:
        max=num
print(f"El numero mas grande ingresado fue: {max}")
#22)Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. 
# La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
par_numbers = 0

while True:
    num = int(input("Ingrese un número entero positivo (-1 para salir): "))
    
    if num == -1:
        break  
    
    if numero <= 0:
        print("Por favor, ingrese un número entero positivo.")
    else:
        sum_digits = sum(int(digit) for digit in str(num))
        print(f"La suma de los dígitos de {num} es {sum_digits}.")
        
        if num % 2 == 0:
            par_numbers += 1

print(f"Total de números pares ingresados: {par_numbers}")
#23)Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.
num=2.3
total=0
while num!=0:
    num=float(input("Ingrese un numero,ingrese 0 para salir del bucle"))
    total+=num
#24)Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.
num=2.3
total=0
while num!=0:
    num=float(input("Ingrese un numero,ingrese 0 para salir del bucle"))
    if num<0:
        print("No ingrese numero negativos")
    else:
        total+=num
if total>1000:
    print(f"El total a pagar es {total-(total*0.10)} se le aplico un descueto por superar los $1000 pesos en su compra")
else:
    print(f"El total a pagar es: {total}")
#25)Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1.
num = int(input("Ingrese un número entero positivo: "))
factorial = 1
if num < 0:
    print("El factorial no está definido para números negativos.")
elif num == 0:
    print("El factorial de 0 es 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"El factorial de {num} es {factorial}.")