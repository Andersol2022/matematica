from random import randint
from time import sleep


class Print_especial:
    def __init__(self, dividir=True, traço=True, traço_baixo=True, mais=True, representa=True, menos=True, vezes=True, sair=True, oculto_menos=True, oculto_vezes=True, oculto_divisao=True, entrada1=True):
        self.oculto_divisao = oculto_divisao
        self.entrada1 = entrada1
        self.mais = mais
        self.vezes = vezes
        self.oculto_vezes = oculto_vezes
        self.sair = sair
        self.dividir = dividir
        self.representa = representa
        self.menos = menos
        self.traço = traço
        self.traço_baixo = traço_baixo
        self.oculto_de_menos = oculto_menos

    def menor(self):
        print('--------------------------')

    def anderline(self):
        print('__________________________')

    def entrada(self):
        en1 = int(input('Digita um numero: '))
        en2 = int(input('Digita um numero: '))

    def adição(self, a, b):
        print('\033[35m= {} + {} = {}'.format(a, b, a + b))

    def divisao(self, a, b):
        print('\033[35m= {} / {} = {}'.format(a, b, a / b))

    def subtracao(self, a, b):
        print('\033[35m= {} - {}'.format(b, a))

    def multiplicaçao(self, a, b):
        print('\033[35m= {} x {} = {}'.format(a, b, a * b))

    def oculto(self, a, b):
        print('\033[35mx + {} = {}'.format(a, b))

    def oculto_sub(self, a, b):
        print('\033[35mx - {} = {}'.format(a, b))

    def oculto_multi(self, a, b):
        print('\033[35my x {} = {}'.format(a, b))

    def oculto_div(self, a, b):
        print('\033[35mx / {} = {}'.format(a, b))

    def saindo(self):
        print('saindo.')
        sleep(1)
        print('saindo..')
        sleep(1)
        print('saindo...')
        print('________________________')
        print('saindo.')
        sleep(1)
        print('saindo..')
        sleep(1)
        print('saindo...')
        print('________________________')
    pass


def tabuada():
    p = Print_especial()
    p.anderline()
    maximo = int(input('Digita um numero: '))
    for x in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}:
        p.multiplicaçao(x, maximo)
    p.anderline()


def equacoes():
    contador = 1
    p = Print_especial()
    stop = True
    try:
        while stop:
            a = randint(1, 50)
            b = randint(50, 100)
            mas = int(input('''
\033[33m1 ===> Adiçao;
\033[36m2 ===> Subtração;
\033[37m3 ===> Multiplicação;
\033[35m4 ===> Divisão
\033[34m=====> Resposta: '''))

            if mas == 1:
                total = b - a
                p.oculto(a, b)
                valor = int(input('Qual è o valor que representa x?: '))
                if total == valor:
                    print('parabens')
                    stop = False
                else:
                    print('Errado')
                    p.menor()
                    p.oculto(a, b)
                    p.subtracao(b, a)
                    print('= {}'.format(total))
                    print('A resposta e {}'.format(total))
                    p.menor()

            if mas == 2:
                total = b + a
                p.oculto_sub(a, b)
                valor = int(input('Qual è o valor que representa x?: '))
                if total == valor:
                    print('parabens')
                    stop = False
                else:
                    print('Errado')
                    p.menor()
                    p.oculto_sub(a, b)
                    p.adição(b, a)
                    print('= {}'.format(total))
                    print('A resposta e {}'.format(total))
                    p.menor()


            if mas == 3:
                total = b / a
                p.oculto_multi(a, b)
                valor = float(input('Qual è o valor que representa x?: '))
                if total == valor:
                    print('parabens')
                    stop = False
                else:
                    print('Errado')
                    p.menor()
                    p.oculto_multi(a, b)
                    p.divisao(b, a)
                    print('{:.0f}'.format(total))
                    print('A resposta e {}'.format(total))
                    p.menor()


            if mas == 4:
                total = b * a
                p.oculto_div(a, b)
                valor = float(input('Qual è o valor que representa x?: '))
                if total == valor:
                    print('parabens')
                    stop = False
                else:
                    print('Errado')
                    p.menor()
                    p.oculto_div(a, b)
                    p.multiplicaçao(b, a)
                    print('{:.1f}'.format(total))
                    print('A resposta e {}'.format(total))
                    p.menor()

    except:
        p.saindo()
        print('\033[36m___FIM DO JOGO___')
        print('\033[36m___{} Tentativa___'.format(contador))