# TODO
############################################################################
def frac():
    """Funcçao para definir fracçoes"""
    numerador = int(input('Digita o numerador: '))
    denominador = int(input('Digita o denominador: '))
    print('A fracao e {} sobre {}'.format(numerador, denominador))
    return numerador, denominador

def sum_fracao(fraA_1, fraA_2):
    """Somar duas fracçoes com adiçao"""
    if fraA_1[1] == fraA_2[1]:
        final = fraA_1[0] + fraA_2[0]
        print('A soma de {} sobre {} + {} sobre {} e igual a {} sobre {}'.format(fraA_1[0], fraA_1[1], fraA_2[0], fraA_2[1], final, fraA_2[1]))
        return final, fraA_1[0], fraA_2[1]
    else:
        print('ERROR: Os demoniandores sao diferentes')

def add(fraA_1, fraA_2):
    """Somar duas fracçoes com adiçao"""
    if fraA_1[1] == fraA_2[1]:
        final = fraA_1[0] + fraA_2[0]
        print('A soma de {} sobre {} + {} sobre {} e igual a {} sobre {}'.format(fraA_1[0], fraA_1[1], fraA_2[0], fraA_2[1], final, fraA_2[1]))
        return final, fraA_1[0], fraA_2[1]
    else:
        print('ERROR: Os demoniandores sao diferentes')


def multiplicaçao(fraA_1, fraA_2):
    """Somar duas fracçoes com a multipliçao"""
    final = fraA_1[0] * fraA_2[0]
    final_2 = fraA_1[1] * fraA_2[1]
    print(f'{fraA_1[0]}/{fraA_1[1]} x {fraA_2[0]}/{fraA_2[1]} = {final}/{final_2}')
    return final, final_2


def comparaçao(fraA):
    """Funçao para comparar numerador e o denominador de uma fracçao"""
    if fraA[0] <= fraA[1]:
        print('{} sobre {} e menor do que a unidade'.format(fraA[0], fraA[1]))
    elif fraA[0] == fraA[1]:
        print('{} sobre {} e igual ao denominador, a fraccao e igual a unidade'.format(fraA[0], fraA[1]))
    elif fraA[0] >= fraA[1]:
        print('{} sobre {} e maior que o denominador, a fraccao e maior que a unidade'.format(fraA[0], fraA[1]))
    return fraA[0], fraA[1]


def form_mista(fraA):
    """Partes inteiras de uma fracçao"""
    if fraA[0] <= fraA[1]:
        print('a fracçao {} sobre {} nao tem parte inteira'.format(fraA[0], fraA[1]))
    else:
        print('a fracçao {} sobre {} e uma fracção mista a parte inteira e {}'.format(fraA[0], fraA[1], int(fraA[0] / fraA[1])))
    return fraA[0],fraA[1]


def equivalencia(fraA):
    print('a classe equivalencia da facçao {} sobre {}'.format(fraA[0] / 6, fraA[1] / 6))
    return fraA[0], fraA[1]


def comparaçao_de_numeros(fraA_1, fraA_2):
    """Funcçao para comarar a diferenca de fracçoes"""
    if fraA_1[0] == fraA_2[0]:
        print('Como os numeradores sao iguais vou comparar os denominadores {} < {}'.format(fraA_1[1], fraA_2[1]))
    if fraA_1[1] == fraA_2[1]:
        print('Como os denominadores sao iguais vou comparar os numeradores {} > {}'.format(fraA_1[0], fraA_2[0]))
    return fraA_1, fraA_2

#END
#################################################
def main():
    #Funçao principal#
    print('Intrudua a fraccao')
    a = frac()
    form_mista(a)
    print('Introduz a segunda fraccão')
    b = frac()
    multiplicaçao(a, b)
    equivalencia(a)
    comparaçao_de_numeros(a, b)


if __name__ == '__main__':
    main()