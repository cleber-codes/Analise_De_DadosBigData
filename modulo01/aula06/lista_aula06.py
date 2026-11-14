### LISTAS ###

# ÍNDICES: 0 1 2 3 4

compras = ["arroz", "sabão", "pão", "açucar", "feijão"]

compras2 = ["amaciante", "papel toalha", "farinha", "maçã" , "pão de forma"]
    
print(len(compras2))
print(compras2[0:8:1])


compras_final = compras + compras2
print("compras_final")


compras3 = [
    "laranja"
    "maçã"
    "hamburguer"
    "sal"
]

compras_final = compras_final + compras3
# print(compras_final)

# compras_final += ["café"]

compras_final.insert(2,"café")
# print("compras_final")

compras_dezembro=compras_final.copy()
print(compras_dezembro)

compras_final.count("maçã")

compras_final.clear()

##tuplas

#tupla_compras = tuple(compras_dezembro)




filmes_final_semana = {"O Menino a A Garça", 
                       " As Branquelas", 
                       "Premonição", 
                       "Avengers", 
                       "Diario de uma Paixão"
                       }

# print(filmes_final_semana)
for i in filmes_final_semana:
    print(i)


###### dicionario##


filmes = {
    "Titanic": 1997,
    "Como treinar o seu dragão": 2010

}

nomes_filmes = ["titanic", "shrek",]
ano_lançamento_filmes = [1997,2001]
genero_filmes = ["Drama/Romance", "comédia/Animação"]
indicacoes_oscar = ["sim","sim"]

titanic_info = ["tITANIC", 1997, "Drama/Romance", "Sim"]
