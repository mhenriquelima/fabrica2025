print("se usar letra vai toma break")
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
        print("Seu histórico: {}".format(historico))

while Is_running == True:
    calculo = input("""
    ql o calculo 
    [0] - soma 
    [1] - subtracao 
    [2] - multiplicacao 
    [3] - divisao
    [4] - mostrar historico
    [5] - limpar
    > """)
    try:
        result = int(calculo) + 1
    except TypeError:
        print("reinicie")
        break
    except ValueError:
        print("reinicie")
        break
    
    if int(calculo) <= 3:
        n1 = float(input("n1 > "))
        n2 = float(input("n2 > "))
        calculoList = [cal.adcionar(n1,n2),cal.subtrair(n1,n2),cal.multiplicar(n1,n2),cal.dividir(n1,n2),cal.mostrar_historico(),]
        print(calculoList[int(calculo)])
        historico.append(calculoList[int(calculo)])
    elif int(calculo) == 4:
        cal.mostrar_historico()
    elif int(calculo) == 5:
        historico.clear()
    else:
        print("ESCOLHA UMA OPCAO VALIDA")