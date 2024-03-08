#!/usr/bin/env python3
# from typing import

# Programas do desafio

# Sequencia de Fibonacci
def fibonacci(numero: int) -> bool:
    print(f"Verificando se o número {numero} faz parte da sequência de Fibonacci...")
    if numero == 0:
        return True
    elif numero == 1:
        return True
    else:
        sequencia = [0, 1]
        ultimo_numero = 0
        while ultimo_numero < numero:
            ultimo_numero = sequencia[-1] + sequencia[-2]
            sequencia.append(ultimo_numero)
        if ultimo_numero == numero:
            return True
        else:
            return False

print(fibonacci(4))

def inverte_string(string: str) -> str:
    print(f"Invertendo a string {string}...")
    string_reversa = string[::-1]
    return string_reversa

print(inverte_string("nome"))
