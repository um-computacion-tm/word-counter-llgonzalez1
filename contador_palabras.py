def count_words(frase):
    lista_palabras= frase.split()
    contador= {}
    for palabra in lista_palabras:
        if palabra in contador:
            contador[palabra] +=1
        else:
            contador[palabra] =1
    return contador



