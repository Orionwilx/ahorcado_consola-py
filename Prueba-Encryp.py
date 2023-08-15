
caractere_select = "x"

def Encrypt(frase, caractere):
    encrypt = ""

    for letra in frase:
        if letra.lower() in "aeiouáéíóú":
            if letra.isupper():
                encrypt += caractere.upper()
            else:
                encrypt += caractere
        else:
            encrypt += letra
    
    return encrypt


while True:
    print(Encrypt(input("Ingrese una frase\n>"), caractere_select))

    print("\nIngresa\n [1] Para escribir otra frase."
          "\n [2] Para salir del programa.")
    
    option = input(">")
    
    if option == "2":
        break
    
