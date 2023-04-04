def roman_to_decimal(roman):
    
    total = 0
    nuevo_valor= 0
    for letter in roman:
        if letter == 'I':
            valor = 1
        elif letter == 'V':
            valor = 5
        elif letter == 'X':
            valor = 10
        elif letter == 'L':
            valor = 50
        elif letter == 'C':
            valor = 100
        elif letter == 'D':
            valor = 500
        elif letter == 'M':
            valor = 1000
        if valor> nuevo_valor:
            total += valor - 2* nuevo_valor
        else:
            total += valor
        nuevo_valor = valor
    return total
print(roman_to_decimal('XL'))