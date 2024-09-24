texto = input("Ingrese una cadena de texto: ")
vocales = "aeiouAEIOU"
resultado = "".join([letra for letra in texto if letra not in vocales])
print(resultado)