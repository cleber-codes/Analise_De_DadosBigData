
from banco_dados import *


def listar_planos_streaming(banco_dados):
    
    print("=" * 50)
    print("          CATÁLOGO DE PLANOS STREAMING")
    print("=" * 50)

    for id_plano, info in banco_dados["planos_streaming"] .items():

        print(f"ID do Plano: {id_plano}")
        print(f"Nome: {info["nome"]}")
        print(f"Mensalidade: R$ {info["mensalidade"]:.2f}")
        print(f"Telas simultâneas: {info["telas_simultaneas"]}")

        print("=" * 50)

    print("ATENÇÂO: Contrataçôes dde 12 meses ou mais")
    print("recebem 15% de desconto direto no plano.")
    print("=" * 50)



listar_planos_streaming(banco_dados)