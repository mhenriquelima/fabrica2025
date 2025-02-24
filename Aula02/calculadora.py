historico = []
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
        if n2 == 0:
            result = "indeterminado"
        else:
            result = n1 / n2
        return result
    def mostrar_historico():
        print(historico)
        
while True:
    calculo = int(input("""ql o calculo 
    [0] - soma 
    [1] - subtracao 
    [2] - multiplicacao 
    [3] - divisao
    [4] - mostrar historico
    [5] - limpar
    > """))

    if calculo <= 3:
        n1 = int(input("n1 > "))
        n2 = int(input("n2 > "))
        calculoList = [cal.adcionar(n1,n2),cal.subtrair(n1,n2),cal.multiplicar(n1,n2),cal.dividir(n1,n2),cal.mostrar_historico()]
        print(calculoList[calculo])
        historico.append(calculoList[calculo])
    elif 4 == calculo:
        cal.mostrar_historico()
    elif 5 == calculo:
        historico.clear()
    else:
        print("escolha uma opcao valida")