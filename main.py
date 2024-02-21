#homework p47
def bio(name,born,pronoun):
    yers_old = born-2024
    age_in_67 = born+67
    print(name," , she was born in",born)
    print(name,"  ,she will turn",yers_old , "this year !")
    print(name ," , well be 67 in " ,age_in_67)

bio("retaj",2005,"she")

#homework p43
def quadraticFormula1(a, b, c):
    y = b**2 - 4*a*c
    return y
def quadraticFormula2(a, b, c):
    y = b**2 + 4*a*c
    return y