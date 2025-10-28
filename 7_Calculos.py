# Calculos.py
# -- coding: utf-8 --
import os

def _limpar_tela():
    # limpa a tela de forma segura (Windows / Unix)
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        pass

def _ler_numero(prompt):
    """Lê um número float com tratamento de erro; retorna None se cancelado/errado."""
    try:
        s = input(prompt).strip()
        return float(s)
    except ValueError:
        print("Entrada inválida: por favor digite um número válido.")
        return None
    except (KeyboardInterrupt, EOFError):
        print("\nEntrada interrompida pelo usuário.")
        return None

def calculos():
    """
    Submenu de cálculos básicos.
    Use import Calculos e chame Calculos.calculos() no menu principal.
    """
    while True:
        _limpar_tela()
        print("\n=== CÁLCULOS ===")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Voltar ao menu principal")
        opc = input("Escolha uma opção: ").strip()

        if opc == "1":  # Adição
            a = _ler_numero("Número 1: ")
            if a is None:
                input("Pressione ENTER para continuar...")
                continue
            b = _ler_numero("Número 2: ")
            if b is None:
                input("Pressione ENTER para continuar...")
                continue
            print(f"Resultado da adição: {a + b}")

        elif opc == "2":  # Subtração
            a = _ler_numero("Número 1: ")
            if a is None:
                input("Pressione ENTER para continuar...")
                continue
            b = _ler_numero("Número 2: ")
            if b is None:
                input("Pressione ENTER para continuar...")
                continue
            print(f"Resultado da subtração: {a - b}")

        elif opc == "3":  # Multiplicação
            a = _ler_numero("Número 1: ")
            if a is None:
                input("Pressione ENTER para continuar...")
                continue
            b = _ler_numero("Número 2: ")
            if b is None:
                input("Pressione ENTER para continuar...")
                continue
            print(f"Resultado da multiplicação: {a * b}")

        elif opc == "4":  # Divisão
            a = _ler_numero("Número 1 (dividendo): ")
            if a is None:
                input("Pressione ENTER para continuar...")
                continue
            b = _ler_numero("Número 2 (divisor): ")
            if b is None:
                input("Pressione ENTER para continuar...")
                continue
            if b == 0:
                print("Erro: divisão por zero não é permitida.")
            else:
                print(f"Resultado da divisão: {a / b}")

        elif opc == "5":  # Voltar
            break

        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione ENTER para continuar...")