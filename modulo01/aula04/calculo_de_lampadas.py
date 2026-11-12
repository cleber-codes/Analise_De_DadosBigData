### Cálculo de lâmpadas ###

largura = float(input("Digite a largura do cômodo em mêtros:"))
comprimento = float(input("Digite a comprimento do cômodo em mêtros:"))

area = largura * comprimento

potencia_necessaria = largura * comprimento * 3 

potencia = float(input("digite a potência da lâmpada em watts:"))

potencia_necessaria = area * 3 

bocais = area / 3

lampadas = potencia_necessaria / potencia

print("quantidade de lampadas:", lampadas)
print("potencia necessaria", potencia_necessaria)
print("quantidade de bocais:", bocais)







