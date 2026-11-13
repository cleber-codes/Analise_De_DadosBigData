##### Quantidade de Caixas de Azulejos #####

# Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento,
# largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em
# todas as suas paredes (considere que não será descontada a área ocupada por portas e
# janelas). Cada caixa de azulejos possui 1,5 m²


comprimento = float(input("Digite o comprimento da cozinha:"))
largura = float(input("Digite a largura da cozinha:"))
altura = float(input("Digite a altura da cozinha:"))

area = 2 * (comprimento + largura) * altura

caixas = area / 1.5

print("Área das paredes:", area, "m²")
print("Quantidade de caixas:", caixas)