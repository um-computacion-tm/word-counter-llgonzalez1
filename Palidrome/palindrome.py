def palindrome (frase): 
    palabra= frase.replace(' ', '')
    palabra_dada_vuelta= palabra[::-1]
    if palabra == palabra_dada_vuelta:
        return True
    else: 
        return False



