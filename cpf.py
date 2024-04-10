def validar_cpf_teste(n):

    if n.count(n[0]) == len(n):
        return False
    
    if len(n) != 11:
        return False
    
    check1 = 0
    check2 = 0

    for i, x in enumerate(n[0:9]):
        check1 += int(x) * (10 - i)

    digito1 = (check1 * 10) % 11
    if digito1 == 10:
        digito1 = 0

    for i, x in enumerate(n[0:10]):
        check2 += int(x) * (11 - i)

    digito2 = (check2 * 10) % 11
    if digito2 == 10:
        digito2 = 0
        
    if (digito1 == int(n[-2]) and digito2 == int(n[-1])):
        return True
    else:
        return False
