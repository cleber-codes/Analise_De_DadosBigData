
### Desafio_2 ###

for aluno in range(1,11):
    print("aluno", aluno)


    nota_1 = float(input("Digite a primeira nota:"))
    nota_2 = float(input("Digite a segunda nota:"))
    nota_3 = float(input("Digite a terceira nota:"))
    nota_4 = float(input("Digite a quarta nota:"))

    media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
    print("media",media)


    if media >= 7:
        print("aprovado")

    elif media >= 5 and media < 7:
        print("recuperação")

    else:
        print("reprovado")

