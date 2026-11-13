
#### Cadastros dos candidatos ###

for candidato in range(1,13):
    print("Cadastro do candidado", candidato)

    ano = int(input("Digite o ano de nascimento:"))
    
    idade = 2026 - ano

    if idade < 18:
        print("Candidato menor de idade. Não pode participar.")

    else:
        print("candidato maior de idade. Cadastro permitido.")

        telefone = input ("Digite seu telefone:")
        email = input("Digite o seu email:")


        print("idade:", idade)
        print("Telefone:",telefone)
        print("Email:", email)
        print("cadastro realizado!")

        