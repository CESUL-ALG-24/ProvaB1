valor_investido = float(input("Informe o valor investido: "))
taxa = float(input("Informe a taxa anual: "))
tempo = int(input("Informe o tempo (em anos): "))

total = (valor_investido * taxa * tempo) / 100

print("O valor total será R$", total)
