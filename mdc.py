# função que permite calcular o MDC
def MDC(a, b):
    while (b != 0):
        resto = a % b
        a = b
        b = resto

    return a


# função principal do programa
def main():
    print("Este programa permite calcular o MDC\n")
    x = int(input("Digita o primeiro valor: "))
    y = int(input("Diggita o segundo valor: "))
    print(f"\nO MDC de ({x} e {y}) = {MDC(x, y)}")


if __name__ == "__main__":
    main()