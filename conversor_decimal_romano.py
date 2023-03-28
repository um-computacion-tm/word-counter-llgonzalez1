def decimal_to_roman(decimal):
    if decimal <= 3:
        return 'I' * decimal
    elif decimal == 4:
        return 'IV'
    elif decimal in range (5,9):
        return 'V'+ decimal_to_roman(decimal-5)
    elif decimal == 9: 
        return 'IX'
    elif decimal in range (10,40):
        return (('X'*(decimal//10))+decimal_to_roman(decimal %10))
    elif decimal in range (40,50):
        return ('XL'+decimal_to_roman(decimal%40))
    elif decimal in range (50,90):
        return ('L'+ decimal_to_roman(decimal -50))
    elif decimal in range (90,100):
        return ('XC'+ decimal_to_roman(decimal-90))
    elif decimal in range (100,400):
        return (('C'* (decimal //100)) + decimal_to_roman(decimal%100))
    elif decimal in range (400,500):
        return ('CD' + decimal_to_roman(decimal-400))
    elif decimal in range (500,900):
        return ('D'+ decimal_to_roman(decimal-500))
    elif decimal in range (900,1000):
        return ('CM' + decimal_to_roman(decimal-900))
    elif decimal ==1000:
        return 'M'
