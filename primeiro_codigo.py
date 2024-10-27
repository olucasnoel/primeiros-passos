
#inicio do código - entrada de dados
a = input('Digite algo: ')
print('o tipo primitivo desse valor é ', type(a))
print('Só tem espaço? ', a.isspace())    #variavel e ISSPACE() dentro do print faz com ele teste verdadeiro ou falso
print('É um número? ', a.isnumeric())       #variavel e o .is dentro da print mostra as informações do dado inserido na variavel
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maíusculas? ', a.isupper())
print('Está em mainúsculas? ', a.lower())   
print('Está capitalizada? ', a.title())

#repetir a string várias vezesz
print ('='*20) #* fora da aspa dentro do ()

#o {} seguido do .format e a variavel, retorna uma mensagem para o usuário.
#exemplo: input irá pedir o nome e o nome é a variável. na lina 20 ele vai retornar a mensagem estabelecida e o nome da váriavel que foi digitada.

nome = input ('Qual é o seu nome? ')
print('Prazer em te conhecer, {}'.format(nome))
#########
#######
#n1 e n2 são variáveis. int é inteiro e input é pra aparecer mensagem na tela. 
#s, m, d, di, e são funções matemáticas nativas do interpretador de texto

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} e a \n divisão é {:.3f}'.format(s, m, d), end='') #as chaves são pra apresentar o valor das variáveis na fase de saída de dados
print('Divisao inteira {} e potência {}'.format(di, e))
#o {:3f} é para dar o resultado com somente 3 casas decimais. o f é float
#o end='' é pra apresentar o resultado tudo na mesma linha
#o \n é pra quebrar a linha


####### Lê um número inteiro do usuário #####
numero = int(input("Digite um número inteiro: "))

# Calcula o sucessor e o antecessor
antecessor = numero - 1
sucessor = numero + 1

# Mostra o antecessor e o sucessor
print(f"O antecessor de {numero} é {antecessor} e o sucessor é {sucessor}.")

## crie um algoritmo que leia um numero e mostre seu dobro, seu triplo a raiz quadrada
numero  = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** 0.5
print(f'o dobro desse numero é {dobro}, o triplo desse é o {triplo}, a raiz quadrada é {raiz_quadrada}. ')

#####desenvolver um programa que leia duas notas de um aluno, calcule e mostre sua média
nota1 = 70
nota2 = 80
media = (nota1 + nota2) /2 
print(media)


##escrever um programa que leia um valor em metros e exiba convertido em centimetros e milimetros##
metros = 14
em_centimetros = metros * 10
em_milimetros = metros * 100
print(f' {metros} Metros convertido em centímetros é {em_centimetros} e em milímetros é {em_milimetros}. ')


## esse daqui quebrou minha cabeça kkkk
##laço de repetição
########    FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E MOSTRE NA TELA A SUA TABUADA.

numero = int(input('Digite um número: '))
print(f"Tabuada do {numero}:") #O f é pra deixar oque está dentro de {} apresentando o valor que o usuário digitar

for i in range(1, 11): #é aqui que ta a parada. o laço de repetição. "for i in" i é uma variável. "(1: 11):" é a pra fazer 10x em ordem

    resultado = numero * i #aqui são as variáveis fazend oa operação

    print(f'{numero} x {i} = {resultado}') #variáveis sempre entre {}


    ##CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR.
    ##CONSIDERANDO QUE O US$ 1.00 = R$: 3.27 (ÉPOCA BOA NÉ?!)

    carteira = float (input('Digite seu saldo: ')) #coloquei o float pois os resultados que precisam de casas decimais(números reais), são números flutuantes ou floats
    dolares = carteira * 3.27
print(f'Com o seu saldo {carteira} você poderá comprar dolares: {dolares}')

##faça um programa que leia a largura e a altura de uma parede em metros.
#calcule sua área e a quantidade necessária de tinta pra pintar ela. ##sabendo que cada litro de tinta rende 2m2

largura = float (input('Digite a largura: '))
altura = float (input('Digite a altura: '))
area = largura * altura
litro_tinta = area *0.5
print(f'A área da sua parede é: {area}m2 e quantidade de litros de tinta {litro_tinta} necessário para printar é: ')

    
##preço = input('Digite o preço: ')
percentual = 50/100
preço_desconto = preço_desconto  - (percentual / 100)
print(f'Seu desconto é de 5%, então seu preço com desconto é: {preço_desconto}')

# Solicita ao usuário o preço do produto
preco = float(input("Digite o preço do produto: R$ "))

# Calcula o desconto de 5%
desconto = preco * 0.05
novo_preco = preco - desconto

# Mostra o novo preço com desconto
print(f"O novo preço com 5% de desconto é: R$ {novo_preco:.2f}")


##faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float (input('Seu salário atual: '))
aumento = salario * 0.15
resultado = salario + aumento
print(f'Seu salário atual é {salario} e seu novo salário com aumento de 15% é: {resultado}')

##              MÓDULOS       ##
#IMPORTAR BIBLIOTECAS. 
#NA PRIMEIRA LINHA "import math" math é o nome da biblioteca
#para importar um operador aritmético, math. nome do operador e (x)
import math
num = int (input('digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} igual a {}'.format(num, raiz))
### no .format eu definno a ordem e consigo puxar operações aritméticas da biblioteca
print('A raiz de {} igual a {}'.format(num, math.ceil(raiz))) #   math.ceil arredonda pra cima
#  math.floor arredonda o valor pra baixo.

#também tem como definir quantas casa decimais vão apresentar no resultado
# faz assim: "{:.3f}" significa 3 casas depois do .
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))


##    oturo exemplo de importação. dessa vez vou importar apenas o operador e não a biblioteca toda
from math import sqrt, floor  # o comando 'from math import' seleciona oq importar
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))

# exemplo de outra biblioteca para importação e usabilidade
import random #essa biblioetca define um numero aleatorio
num = random.random()
print(num)

#pode definir caracteristicas do numero a ser gerado, como por ex: int, float
import random
num = random.randint(1, 10)
print(num)



