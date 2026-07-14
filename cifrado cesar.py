def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            nueva_pos = (ord(char) - base + desplazamiento) % 26
            resultado += chr(base + nueva_pos)
        else:
            resultado += char
    return resultado


def descifrar_cesar(texto, desplazamiento):
    return cifrar_cesar(texto, -desplazamiento)


def menu():
    print("=== Cifrado César ===")
    print("1. Cifrar texto")
    print("2. Descifrar texto")
    print("3. Salir")

    while True:
        opcion = input("\nElige una opción (1-3): ").strip()

        if opcion == "1":
            texto = input("Ingresa el texto a cifrar: ")
            try:
                desplazamiento = int(input("Ingresa el desplazamiento (ej: 3): "))
            except ValueError:
                print("El desplazamiento debe ser un número entero.")
                continue
            texto_cifrado = cifrar_cesar(texto, desplazamiento)
            print(f"Texto cifrado: {texto_cifrado}")

        elif opcion == "2":
            texto = input("Ingresa el texto a descifrar: ")
            try:
                desplazamiento = int(input("Ingresa el desplazamiento usado: "))
            except ValueError:
                print("El desplazamiento debe ser un número entero.")
                continue
            texto_descifrado = descifrar_cesar(texto, desplazamiento)
            print(f"Texto descifrado: {texto_descifrado}")

        elif opcion == "3":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()