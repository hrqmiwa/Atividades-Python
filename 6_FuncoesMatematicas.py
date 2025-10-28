# -*- coding: utf-8 -*-
import os
import math
import random


# Função para calcular a raiz quadrada
def raiz_quadrada() :
    numero = float (input("Digite um numero para calcular a raiz quadrada : "))
    if numero < 0:
        print ("Não é possivel calcular a raiz quadrada de número negativo")
    else:
        resultado = math.sqrt(numero)
        print(f"A raiz quadrada de {numero} é {resultado}")
    input("Pressione qualquer tecla para continuar...")


# Função para calcular potencia
def potencia ():
    base = float(input("Digite a base: "))
    expoente = float(input("Digite o expoente: "))
    resultado = math.pow (base, expoente)
    print(f"{base} elevado a {expoente} é igual a {resultado}")
    input ("Pressione qualquer tecla para continuar...")


# Função para gerar número randomico
def numero_aleatorio():
    inicio = int(input("Digite o valor inicial do intervalo: "))
    fim = int(input("Digite o valor final do intervalo: "))
    if inicio > fim:
        print ("O valor inicial deve ser menor ou igual ao valor final!")
    else:
        numero = random.randint(inicio, fim)
        print(f"Número aleatorio gerado entre {inicio} e {fim}: {numero}")
    input("Pressione qualquer tecla para continuar...")

# Programa pricipal com menu 
def main():

        while True:
            os.system("cls")
            print("\n=== MENU DE OPERAÇÕES ===" )
            print("1 - Raiz Quadrada")
            print("2 - Potencia")
            print("3 - Número Randomico") 
            print("4 - Sair")
            
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                raiz_quadrada()
            elif opcao == '2': #elseif opcao == '2':
                print("Saindo do programa.. Até logo!")
                break 
            else:
                print("Opção inválida! Tente novamente.")

#Executa o programa 
if __name__ == "__main__":
   main()


    