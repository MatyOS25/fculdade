def converter_idade_dias():
    '''Retorna o valor em dias de anos,meses + dias da idade de uma pessoa'''
    anos = int(input("Informe os anos: "))
    meses = int(input("Informe os meses: "))
    dias = int(input("Informe os dias: "))

    if anos < 0 :
        anos = int(input("Valor de anos inválido. Informe os anos: "))
    elif meses < 0 :
        meses = int(input("Valor de meses inválido. Informe os meses: "))
    elif dias < 0 :
        dias = int(input("Valor de dias inválido. Informe os dias: "))
    else :
        anos_dias = 0

    anos_dias = anos*365
    meses_dias = meses*30
    dias_total = anos_dias + meses_dias + dias

    print(f"A idade em dias, é de aproximadamente {dias_total} dias.")

converter_idade_dias()