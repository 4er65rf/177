def ubicadorDeVocales(cadena):

    cadena = cadena.lower()

    vocales="aeiou"

    ubicaciones={vocal:[]for vocal in vocales}

    for indice,letra in enumerate(cadena):
        if letra in ubicaciones:
            ubicaciones[letra].append(indice)
    return ubicaciones

print(ubicadorDeVocales("murcielago"))

print(ubicadorDeVocales("eucalipto"))

print(ubicadorDeVocales("Albericoque"))


