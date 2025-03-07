def contadorDeVocales(cadena):

    cadena = cadena.lower()

    vocales = "aeiou"
    
    conteo = {vocal: cadena.count(vocal) for vocal in vocales}

    return conteo

print(contadorDeVocales("murcielago"))

print(contadorDeVocales("eucalipto"))

print(contadorDeVocales("Albericoque"))
