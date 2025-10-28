import math
import random
import os

def calculadora():
    print("\n=== CALCULADORA ===")
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")
    op = input("Escolha a operação: ")

    if op == '1':
        print(f"Resultado: {n1 + n2}")
    elif op == '2':
        print(f"Resultado: {n1 - n2}")
    elif op == '3':
        print(f"Resultado: {n1 * n2}")
    elif op == '4':
        if n2 != 0:
            print(f"Resultado: {n1 / n2:.2f}")
        else:
            print("Erro! Divisão por zero.")
    else:
        print("Operação inválida!")


def tipos_triangulo():
    print("\n=== TIPOS DE TRIÂNGULO ===")
    a = float(input("Lado A: "))
    b = float(input("Lado B: "))
    c = float(input("Lado C: "))

    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            print("Triângulo EQUILÁTERO!")
        elif a == b or b == c or a == c:
            print("Triângulo ISÓSCELES!")
        else:
            print("Triângulo ESCALENO!")
    else:
        print("Os lados não formam um triângulo!")


def hipotenusa():
    print("\n=== HIPOTENUSA ===")
    co = float(input("Digite o cateto oposto: "))
    ca = float(input("Digite o cateto adjacente: "))
    h = math.hypot(co, ca)
    print(f"A hipotenusa é: {h:.2f}")


def media_mencao():
    print("\n=== MÉDIA COM MENÇÃO ===")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) / 2
    print(f"Média: {media:.1f}")

    if media >= 9:
        print("Menção: Excelente (A)")
    elif media >= 7:
        print("Menção: Bom (B)")
    elif media >= 5:
        print("Menção: Regular (C)")
    else:
        print("Menção: Insuficiente (D)")


def tabuada():
    print("\n=== TABUADA ===")
    num = int(input("Digite um número: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


def equacao_segundo_grau():
    print("\n=== EQUAÇÃO DO 2º GRAU ===")
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b**2 - 4*a*c
    print(f"Delta = {delta}")

    if delta < 0:
        print("Não existem raízes reais.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Raiz única: x = {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")


def joguinho():
    print("\n=== JOGUINHO DE ADIVINHAÇÃO ===")
    numero = random.randint(1, 10)
    tentativas = 0

    while True:
        chute = int(input("Adivinhe o número (1 a 10): "))
        tentativas += 1
        if chute == numero:
            print(f"Parabéns! Você acertou em {tentativas} tentativas!")
            break
        elif chute < numero:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")


def nome_sobrenome():
    print("\n=== NOME E SOBRENOME ===")
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    print(f"Seu nome completo é: {nome} {sobrenome}")


# ===== MENU PRINCIPAL =====
while True:
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Calculadora")
    print("2 - Tipos de Triângulo")
    print("3 - Hipotenusa")
    print("4 - Média com Menção")
    print("5 - Tabuada")
    print("6 - Equação do 2º Grau")
    print("7 - Joguinho de Adivinhação")
    print("8 - Nome e Sobrenome")
    print("9 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        calculadora()
    elif opcao == '2':
        tipos_triangulo()
    elif opcao == '3':
        hipotenusa()
    elif opcao == '4':
        media_mencao()
    elif opcao == '5':
        tabuada()
    elif opcao == '6':
        equacao_segundo_grau()
    elif opcao == '7':
        joguinho()
    elif opcao == '8':
        nome_sobrenome()
    elif opcao == '9':
        print("Saindo... até mais!")
        break
    else:
        print("Opção inválida!")

    input("\nPressione ENTER para voltar ao menu...")
    os.system('cls' if os.name == 'nt' else 'clear')