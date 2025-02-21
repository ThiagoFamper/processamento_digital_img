def primos(x):
    # primos são números naturais maiores que 1, então se for 1 ou menor não é primo.
    if x <= 1:
        return False
    # para x ser primo ele não pode se divísivel por nenhum número entre 2 e a raiz quadrada de x.
    # o + 1 é pq o range para um número antes e o int é para arredondar, já que range não aceita float.
    for i in range(2, int(x ** 0.5) + 1):
        # verifica se o mod da divisão é 0, ou seja, se é dívisivel ou não.
        if x % i == 0:
            # se o mod for 0 então é dívisivel, portanto não é primo.
            return False
    # se nenhum mod for 0 então ele é primo.
    return True

if __name__ == '__main__':
    x = int(input("Informe um número: "))

    if primos(x):
        print("O Número é primo")
    else:
        print("O Número NÃO é primo")