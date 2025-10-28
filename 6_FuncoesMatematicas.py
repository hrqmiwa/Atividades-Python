# -- coding: utf-8 --

import os
import math
import random

# Função para calcular a raiz quadrada
def raiz_quadrada():
    numero = float(input("Digite um número para calcular a raiz quadrada: "))
    if numero < 0:
        print("Não é possível calcular a raiz quadrada de número negativo!")
    else:
        resultado = math.sqrt(numero)
        print(f"A raiz quadrada de {numero} é {resultado}")
    input("Pressione qualquer tecla para continuar...")

# Função para calcular potência
def potencia():
    base = float(input("Digite a base: "))
    expoente = float(input("Digite o expoente: "))
    resultado = math.pow(base, expoente)
    print(f"{base} elevado a {expoente} é igual a {resultado}")
    input("Pressione qualquer tecla para continuar...")

# Função para gerar número aleatório
def numero_aleatorio():
    inicio = int(input("Digite o valor inicial do intervalo: "))
    fim = int(input("Digite o valor final do intervalo: "))
    if inicio > fim:
        print("O valor inicial deve ser menor ou igual ao valor final!")
    else:
        numero = random.randint(inicio, fim)
        print(f"Número aleatório gerado entre {inicio} e {fim}: {numero}")
    input("Pressione qualquer tecla para continuar...")

# Função de cálculos básicos (substitui a importação)
def calculos():
    print("\n=== CALCULADORA BÁSICA ===")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero!")
            input("Pressione qualquer tecla para continuar...")
            return
    else:
        print("Operação inválida!")
        input("Pressione qualquer tecla para continuar...")
        return
    
    print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
    input("Pressione qualquer tecla para continuar...")

# Programa principal com menu
def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("=== MENU DE FUNÇÕES MATEMÁTICAS ===")
        print("1 - Raiz Quadrada")
        print("2 - Potência")
        print("3 - Número Randômico")
        print("4 - Cálculos")
        print("5 - Sair")
        print("====================================")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            raiz_quadrada()
        elif opcao == '2':
            potencia()
        elif opcao == '3':
            numero_aleatorio()
        elif opcao == '4':
            calculos()
        elif opcao == '5':
            print("Saindo do programa... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")
            input("Pressione qualquer tecla para continuar...")

# Executa o programa
if __name__ == "__main__":

    main()
