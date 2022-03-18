class AMPLITUDES:
    def __init__(self, entrada=True):
        self.entrada = entrada

    def soma_de_amplitudes(self, en1, en2, en3):
        def isocelo():
            if en1 == en2 != en3:
                print('com 2 lados iguais chama-se isócelo')
            if en1 == en3 != en2:
                print('com 2 lados iguais chama-se isócelo')
            if en2 == en3 != en1:
                print('com 2 lados iguais chama-se isócelo')

        def escaleno():
            if en1 != en2 != en3:
                print('com todos os lados diferentes chama-se escaleno')

        def equilatero():
            if en1 == en2 == en3:
                print('com essas medidas todas iguais chama-se equilatero')

        isocelo()
        escaleno()
        equilatero()




