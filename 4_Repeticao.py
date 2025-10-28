# -*- coding: utf-8 -*-

# Programa:Multiplicador interativo
import os

while True:
    # Solicita os dois números apo usuario
    os.system("cls")
    numero1 = float (input("Digite o primeiro numero: "))
    numero2 = float (input("Digite o segundo numero: "))

    #Calcula a multiplicaçao 
    resultado = numero1 + numero2
    
    #Exibe o resultado
    print(f"\nO resultado da multipicação de {numero1} x {numero2} é = {resultado} \n")

    # Pergunta se o usuario deseja continuar
    continuar = input("Deseja fazer outro cálculo? (s/n) ").strip().lower()

    # Se o usuario digitar 'n' , o programa encerra
    if continuar != 's':
        print("\nPrograma encerrado. Até logo!")
        break

print ("-" * 40) # separador visual
