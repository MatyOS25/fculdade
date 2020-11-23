alunos = []
Aluno = namedtuple('Aluno', ['nome', 'altura'])


campos = [
    {'label': 'Informe o nome do aluno:', 'valor': 0},
    {'label': 'Informe a altura do aluno (em centimetros):', 'valor': 0},
]

def media_altura(alunos):
    media = calcula_media(alunos)

    alunos_acima_media = []

    for aluno in alunos:
        if int(aluno.altura) > media:
            alunos_acima_media.append(aluno.nome)

    return [media, alunos_acima_media]


def calculo_media(alunos):
    somatorio = 0

    for aluno in alunos:
        somatorio += int(aluno.altura)

    return int(somatorio // len(alunos))


executando = True
while executando:
    aluno = []
    for index, campo in enumerate(campos):
        if not executando: continue

        while True:
            campo['valor'] = input(f"{campo['label']} ") or ''

            if index == 0 and campo['valor'] == 'sair':
                executando = False
                break

            if not campo['valor']:
                print("O valor informado é inválido.")
            elif index == 1 and not campo['valor'].isnumeric():
                print("O valor informado é inválido.")
            else:
                aluno.append(campo['valor'])
                break
    if len(aluno) == 2:
        alunos.append(Aluno(nome=aluno[0], altura=aluno[1]))

# calcula o resultado
resultado = media_altura(alunos)

print(f"Os seguintes alunos estão acima da média de {resultado[0]}cm: ")
print("\n".join(resultado[1]))