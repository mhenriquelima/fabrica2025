#tipos variaveis
nome = "Roldgi" #string (frase/sequencia de caracteres)
idade = 23742 #integer (numero inteiro)
altura = 4.69 #float (numero real)
eh_gordo = True #boolian (verdadeiro ou falso)

#mudar o tipo de variavel
numero = "98" #numero eh string
numeroreal = int(numero) #agr eh integer

#methods (modificações)
frase = "eae"
print(frase.upper()) #>>> vira "EAE"

#operadores matematicos
    #// divisao sem resto >>> 5//2 = 2
    #% resto de uma divisao >>> 5//2 = 1
    #** exponte >>> 5**2 = 25

#ifelse
age = int(input("idade > "))
if 16 <= age < 18: 
   print("jovi")
elif age < 16:
    print("crionça")
else:
   print("arduto")
    
#loop 
#for loop #contador by povo
for i in range(10):
    print("rep num", 1) #>>> conta ate x, sendo range(x), nesse caso até 10

#while loop #contador by eu
counter = 0
max = 10
while counter <= max -1:
    counter += 1
    print(counter)
        
#listas(mutavel), tuplas(imutavel), dicionarios(dados no formato {chave-valor}) e conjuntos(imutavel, sem ordem e sem elementos repetidos)

#listas
names = ["Roldgi", "Mihras", "Matheus"] #>>> lista base
    #append
names.append("Kaio") #>>> adciona kaio a lista anterior
    #insert
names.insert(3, "Vikitu") #>>> adciona vikitu na 4 posicao [0,1,2,3]
    #selecionar
names[0] #>>> se refere ao primeiro item na lista #>>> no caso Roldgi
        #len() #>>> tamanho da lsita
len(names) #>>> 5
        #remove
names.remove("Mihras")
        #pop removee ultimo q foi adcionado, no caso viktiu
names.pop
        #clear
names.clear()

#tuplas (usar qnd vc n vai qrer mudar em parte nenhuma do codigo)
coords = (10,20)
print(coords[0]) #>>> printa primeiro numero da tupla

    #coords[0] = 30 #>>> resulta em erro jaq n se pode mudar uma tupla
    
#dicionarios
dic = {
        "nome": "Carlos",
        "idade": 25,
        "cidade": "JP"
}
print(dic["idade"]) #>>> vai sair 25
    #adciona ao dicionario
dic["profissão"]="engenheiro"
    #deleta
del dic["cidade"]

#conjuntos
numeros = {1,2,3,4,5}
    #add
numeros.add(6)
numeros.add(2) #>>> n funcionaria pq ja tem 2 e n pode repetir em conjuntos
    #remove
numeros.remove(3)
    #operaçoes com conujuntos
A = {1,2,3,4}
B = {3,4,5,6}
    #união
print(A | B) #>>> {1, 2, 3, 4, 5, 6}
    #interseção
print(A & B) #>>> {3, 4}
    #diferença (valores q tem em A e não estao em B) (ordem importa)
print(A - B) #>>> {1, 2}
    #diferença simétrica
print(A ^ B) #>>> {1, 2, 5, 6}

#funcoes (serve pra n repetir o msm código)
def greetings(nome):
    print(f"eae, {nome}!")
greetings("Roldgi") #>>> "eae, Roldgi!"
def soma(a, b):
    return a + b
soma(1, 2) #>>> 1 + 2 = 3
list = ["banana", "maçã", "pêra"]
def append(list, item):
    list.append(item)
append(list, "uva")
#programacao orientada a objetos (POO)
class Pessoa: #>>> criar um objeto (n eh string, nem int, nem bool, nem float)
    def __init__(self,nome,idade,peso,altura): #definir os parametros de tal objeto
        self.nome = nome #>>> seta os valores entregues à função para as variáveis do objeto
        self.idade = idade #>>> "
        self.peso = peso #>>> "
        self.altura = altura #>>> "
    def apresentar(self): #>>> funcão para o objeto
        print(f"Olá meu nome é {self.nome} e eu tenho {self.idade} anos.")
    def calcular_imc(self): #>>> funcão para o objeto
        imc = self.peso / (self.altura ** 2)
        return imc

p1 = Pessoa("Pedro", 25, 70, 1.75)
p1.apresentar()
print(f"Meu imc é {p1.calcular_imc():.2f}")

#==================================DESAFIO==================================#
#|       #criar um objeto (class) e criar funções (methods) para ele        |
#===========================================================================# 

#importar modulos e bibliotecas
import math #>>> biblioteca inclusa no python
    #exemplo de methods q vem
math.sqrt(16) #>>> raiz

import random #>>> mais bibliotecas inclusas
random.randint(1,10) #>>> rng de 1-10

import datetime #>>> mais bibliotecas inclusas
agora = datetime.datetime.now()

#instalar biblioteca com pip ("pip install request" no terminal)

#Respostas Informativas (100 – 199)
#Respostas bem-sucedidas (200 – 299)
#Mensagens de redirecionamento (300 – 399)
#Respostas de erro do cliente (400 – 499)
#Respostas de erro do servidor (500 – 599)  