def valor_orcamento():
    return float (input("\nDigite o valor do orçamento: "))
def valor_MV():
    return float (input("\n Digite o valor do sistema MV: "))
def calculo(a,b):
    return float(a*100)/ b

while True:
    Valor_orc=valor_orcamento()
    Valor_mv=valor_MV()
    resultado=calculo(Valor_orc,Valor_mv)

    print(f"\n Seu resultado e:{resultado:.2f}% ")
