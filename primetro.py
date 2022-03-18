class PERIMETRO:
    def __init__(self, rct=True, qud=True, tri=True):
        self.rct = rct
        self.qud = qud
        self.tri = tri

    def retangulo(self, l, c):
        P = 2 * (c + l)
        print(f'O perimetro dessa figura e {P}cm')

    def quadrado(self, l):
        P = 4 * l
        print(f'O perimetro dessa figura e {P}cm')

    def triangulo(self, l1, l2, l3):
        if l1 == l2 == l3:
            P = 3 * l1
            print(f'O perimetro dessa figura e {P}cm')
        if l1 == l2 != l3:
            P1 = l1 + l2 + l3
            print(f'O perimetro dessa figura e {P1}cm')
        if l1 == l3 != l2:
            P2 = l1 + l2 + l3
            print(f'O perimetro dessa figura e {P2}cm')
        if l2 == l3 != l1:
            P3 = l1 + l2 + l3
            print(f'O perimetro dessa figura e {P3}cm')
        if l2 != l3 != l1:
            P4 = l1 + l2 + l3
            print(f'O perimetro dessa figura e {P4}cm')



