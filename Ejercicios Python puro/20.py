# Escenario 

# Tu programa debe:

#    pedir al usuario que ingrese una palabra.
#    utilizar user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el upper() muy pronto, no te preocupes.
#    emplea la ejecución condicional y la instrucción continue para "devorar" las siguientes vocales A , E , I , O , U de la palabra ingresada.
#   asigna las letras no consumidas a la variable word_without_vowels e imprime la variable en la pantalla.
#    Analiza el código en el editor. Hemos creado word_without_vowels y le hemos asignado una cadena vacía. Utiliza la operación de concatenación para pedirle a Python que combine las letras seleccionadas en una cadena más larga durante los siguientes giros de bucle, y asignarlo a la variable word_without_vowels.

user_word=input("Hola, ingresa una palabra. \n")
user_word = user_word.upper()
word_without_vowels = ""

for letter in user_word:
    if letter!="A":
        if letter!="E":
            if letter!="I":
                if letter!="O":
                    if letter!="U":
                        print (letter) 
                        continue
                    else:
                        word_without_vowels=word_without_vowels+letter
                else:
                    word_without_vowels=word_without_vowels+letter
            else:
                word_without_vowels=word_without_vowels+letter
        else:
            word_without_vowels=word_without_vowels+letter
    else:
        word_without_vowels=word_without_vowels+letter

print("Vocales acumuladas: ",word_without_vowels)
