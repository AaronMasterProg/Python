import string
import random

def password(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation    
    contra = ""
    for i in range (longitud):
        contra += random.choice(caracteres)        
    return contra

longitud=int(input("Dimension de la contraseña: "))

print(password(longitud))
