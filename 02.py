idade = int(input("Informe a idade da pessoa: "))
peso = float(input("Informe o peso da pessoa: "))

if 18 <= idade < 65 and peso < 100:
    print("Você pode andar no brinquedo!")
elif idade < 18:
    idade_acompanhante = int(input("Informe a idade do acompanhante: "))
    peso_acompanhante = float(input("Informe o peso do acompanhante: "))

    peso_total = peso + peso_acompanhante

    if 18 <= idade_acompanhante < 65 and peso_total < 170:
        print("Você pode andar com o acompanhante")
    else:
        print("Você não pode andar no brinquedo")
else:
    print("Você não pode andar no brinquedo")
