#!/usr/bin/env python3
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


def inverte_string(string: str) -> str:
    print(f"Invertendo a string {string}...")
    string_reversa = string[::-1]
    return string_reversa



if __name__ == "__main__":
    print("Resultado dos testes da Target")
    print("Faz parte de Fibonnaci" if fibonacci(4) else "Não faz parte de Fibonacci")
    print("Faz parte de Fibonnaci" if fibonacci(0) else "Não faz parte de Fibonacci")
    print("Faz parte de Fibonnaci" if fibonacci(13) else "Não faz parte de Fibonacci")
    print("Agora vamos inverter strings")
    print(inverte_string("nome"))
