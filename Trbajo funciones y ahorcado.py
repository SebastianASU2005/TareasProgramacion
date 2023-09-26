
#EJERCICIO FUNCIONES 1°
def most (x,y):
    if (x>y):
        return x
    else:
        return y

def least(x,y):
    if (x<y):
        return x
    else:
        return y

x=int(input("Ingrese el valor de x"))
y=int(input("Ingrese el valor de y"))

print(most(x-3,least(x+2,y-5)))

#EJEMPLO DE OTRA FORMA DE APLICAR
def add_diigits(number):
    add=0
    while number !=0:
        digit=number%10
        add +=digit
        number //=10
    return add

total_number=0
while True:
    number=int(input("Ingrese un numero (0 para finalizar)"))
    if number==0:
        break
    sum=add_diigits(number)
    total_number+=number
    print(f"Suma de digitos: {sum}")
sum=add_diigits(total_number)
print(f"La suma de todos los numero ingresado es de: {total_number}")
print(f"Y la suma de sus digitos es igual a: {sum}")

#AHORCADO
import random
def word_select(a):
    num_ramdom=random.choice(a)
    print("Palabra seleccionada")
    word=num_ramdom
    return word
def show_word(letter,word,spaces):
    for i,ch in enumerate(word):
        if ch==letter:
            spaces[i]=letter
    return spaces

list=["phyton","java","variables","funciones","hardware"]
lives=6
while True:
    word=word_select(list)
    spaces=["_"]*len(word)
    while True:
        letter=input("Ingrese una letra")
        if letter in word:
            print (" ".join(show_word(letter,word,spaces)))
        else:
            print("Fallo -1 vida")
            print (" ".join(show_word(letter,word,spaces)))
            lives-=1
        if lives==0:
            print("Perdiste")
            lives=6
            break

        if "_" not in spaces:
            print("!Ganaste¡") 
            break
    while True:
        decision=input("desea jugar de nuevo? SI/NO")
        if decision.lower()=="si":
            print("Reiniciando partida")
            break
        elif decision.lower()=="no":
            print("Muchas gracias por jugar")
            break
        else:
            print("Ingrese una opcion valida")
    if decision=="no":
        break

