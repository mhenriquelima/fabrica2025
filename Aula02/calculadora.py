class cal:
    def adcionar(n1,n2):
        result = n1 + n2
        return result
    def subtrair(n1,n2):
        result = n1 - n2
        return result
    def multiplicar(n1,n2):
        result = n1 * n2
        return result
    def dividir(n1,n2):
        result = n1 / n2
        return result
    def historico(result):
        historico = []
        historico.append(result)
        return historico
    def limpar_historico(historico):
        historico.clear()
        
n1 = int(input("n1 > "))
n2 = int(input("n2 > "))

calculo = input("""ql o calculo 
[0] - soma [1] - subtracao [2] - multiplicacao [3] - divisao > """)

calculoList = [cal.adcionar(),cal.subtrair(),cal.multiplicar(),cal.dividir()]
if calculo <= 4:
    print(calculoList[calculo])
else:
    print("escolha uma opcao valida")
