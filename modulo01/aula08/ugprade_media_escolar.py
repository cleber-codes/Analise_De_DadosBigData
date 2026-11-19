### ugprade mêdia escolar ###

resultados = []

for i in range(1, 6):
    print(f"\nAluno {i}")

    nota1 = float(input("Digite a primeira nota: "))

    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2
    print("media", media)

    if media > 7:
        situacao = "Aprovado"

    elif media >= 5:
        situacao = "Recuperação"

    else:
        situacao = "Reprovado"

    resultados.append(f"Aluno {i} - {situacao}")

    print("\nRESULTADO FINAL")

    for resultado in resultados:
        print(resultado)
