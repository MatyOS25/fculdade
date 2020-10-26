campos = [
    {'label': 'Informe um o tamanho do primeiro lado do triângulo:', 'valor': 0},
    {'label': 'Informe um o tamanho do segundo lado do triângulo:', 'valor': 0},
    {'label': 'Informe um o tamanho do terceiro lado do triângulo:', 'valor': 0},
]

def calcula_tipo_triangulo(x, y, z):
    triangulo = tuple((int(x), int(y), int(z)))
    tipo = False
    for n in triangulo:
        if n > (sum(triangulo) - n):
            return 'Os valores informados não configuram um triângulo'

        if triangulo.count(n) == 3:
            tipo = 'Equilátero'
        elif triangulo.count(n) == 2:
            tipo = 'Isósceles'

    if not tipo: tipo = 'Escaleno'

    return tipo

for campo in campos:
    while True:
        campo['valor'] = input(f"{campo['label']} ") or ''

        if(campo['valor'].isalpha()):
            print("O valor informado é inválido.")
        else:
            break

print(calcula_tipo_triangulo(campos[0]['valor'], campos[1]['valor'], campos[2]['valor']))