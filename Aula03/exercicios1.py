#print("Olá, mundo!")

#nome = "a"
#print(nome)

#def somar(a, b):
#    return a + b

#resultado = somar(10, 5)
#print(resultado)

#numeros = [10, 20, 30]
#indice = int(input("Digite um índice para acessar a lista: ")) 
#try:
#    print(numeros[indice])
#except:
#   print("numero mto alto")

#def dividir(a, b):
#    try:
#        resultado = a / b 
#        return a / b
#  except ZeroDivisionError:
#        print("none")
#    except ValueError:
#        print("none")
    
#num1 = input("Digite o primeiro número: ")
#num2 = input("Digite o segundo número: ")
#try:
#    resultado = dividir(int(num1), int(num2))
#    print(f"Resultado: {resultado}")
#except ValueError:
#    print("none")

#dados = {
#    "nome": "Isaac ",
#    "idade": 25,
#    "cidade": "São Paulo",
#}

#chave = input("Digite a chave que deseja acessar: ")
#try:
#    print(f"O valor da chave '{chave}' é: {dados.get(chave)}")
#except KeyError:
#    print("chave nao encontrada")

#while True :
#    def validar_idade(idade):
#        if idade < 0 or idade > 120:
#            raise ValueError("A idade deve estar entre 0 e 120 anos!")
#        return f"Idade válida: {idade}"
#
#    try:
#        idade = int(input("Digite sua idade: "))
#        print(validar_idade(idade))
#    except ValueError:
#        print("AGAIN")

def calcular_media(notas):
    try:
        soma = sum(notas)
        quantidade = len(notas)
        return soma / quantidade
    except ZeroDivisionError:
        print("notas inválidas")

notas = []

for i in range(0,4):
    try:
        nota = float(input("notas > "))
        if nota < 0 or nota > 10:
            raise ValueError
        notas.append(nota)
        print("nota valida")
    except ValueError:
        notas.append(0)
        print("insira uma nota valida")


media = calcular_media(notas)
print(f"Média: {media:.2f}")