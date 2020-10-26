def triangulo():
    '''Recebe os valores para formar um triangulo, identifica se é possível fazer um triângulo e informa seu tipo'''
    x = float(input("Informe o x: "))
    while x <= 0.00:
        x = float(input("Número inválido, Informe o x: "))
    y = float(input("Informe o y: "))
    while y <= 0.00:
        y = float(input("Número inválido, Informe o y: "))
    z = float(input("Informe o z: "))
    while z <= 0.00:
        z = float(input("Número inválido, Informe o z: "))
    valores = (float(x),float(y),float(z))
    tipo = False
    for val in valores:
        if val > (sum(valores) - val):
            return "Não é triângulo"


        if valores.count(val) == 3:
            tipo = "Equilátero"
        elif valores.count(val) == 2:
            tipo = "Isósceles"
    if not tipo:
        tipo = "Escaleno"
    
    return tipo
print(triangulo())
