import random

def elegir_dificultad():
    print("Selecciona un nivel de dificultad:")
    print("1. Fácil (1-10, 5 intentos)")
    print("2. Medio (1-50, 7 intentos)")
    print("3. Difícil (1-100, 10 intentos)")
    
    while True:
        try:
            eleccion = int(input("Elige 1, 2 o 3: "))
            if eleccion == 1:
                return 10, 5
            elif eleccion == 2:
                return 50, 7
            elif eleccion == 3:
                return 100, 10
            else:
                print("Por favor, elige un número válido (1, 2 o 3).")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

def jugar():
    rango, intentos_max = elegir_dificultad()
    numero_secreto = random.randint(1, rango)
    intentos = 0
    puntos = 0

    print(f"\n¡Adivina el número entre 1 y {rango}!")
    
    while intentos < intentos_max:
        try:
            adivina = int(input("Ingresa tu número: "))
            intentos += 1
            
            if adivina == numero_secreto:
                print(f"🎉 ¡Correcto! Adivinaste el número en {intentos} intento(s).")
                puntos += (rango - intentos * 5)  # Puntuación depende de intentos
                break
            elif adivina < numero_secreto:
                print("📉 Demasiado bajo.")
            else:
                print("📈 Demasiado alto.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    if intentos == intentos_max and adivina != numero_secreto:
        print(f"❌ ¡Se acabaron los intentos! El número era {numero_secreto}.")
    
    print(f"Puntuación final: {puntos}")
    return puntos

def main():
    print("🎮 Bienvenido al juego 'Adivina el Número' 🎮")
    total_puntos = 0
    while True:
        total_puntos += jugar()
        jugar_otra = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
        if jugar_otra != 's':
            print(f"Gracias por jugar. Puntuación total: {total_puntos}")
            break

if __name__ == "__main__":
    main()
