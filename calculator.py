def cut(ini, pol):
    for c in range(ini + 1, len(pol)):
        if pol[c] == '+' or pol[c] == '-':
            return pol[ini:c]
        if c == len(pol) - 1:
            return pol[ini:c+1]

def find_val(pol):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
    
    signal = 1
    if pol[0] == '-':
        signal = -1
    
    coef = ""
    for c in pol:        
        if c == '+' or c == '-':
            continue
        if c in numbers:
            coef += c
        if c not in numbers:
            break
    
    if coef == '':
        coef = 1
    
    coef_int = float(coef)
    return signal*coef_int

def find_expo(pol):

    expo_pos = pol.find('^') + 1
    
    if not expo_pos:
        if pol.find("x") == -1:
            return 0.0
        return 1.0

    expo_str = pol[expo_pos: len(pol)]
    expo_num = find_val(expo_str)
    return expo_num

def fact_pol():
    pol = input("Insira seu polinomio:  ")

    pol = pol.strip()
    pol = pol.replace(" ", "")

    fact = []
    i = 0

    while i < len(pol) - 1:
        pol_aux = cut(i, pol)
        i += len(pol_aux)

        coef = find_val(pol_aux)
        expo = find_expo(pol_aux)
        fact.append([coef, expo])

    return fact

def calculate():
    fact = fact_pol()

    limit = float(input("Insira o limite que deseja calcular: "))

    sum = 0.0

    for coef, exp in fact:
        sum += coef * ((limit) ** exp)

    print(sum)

calculate()

