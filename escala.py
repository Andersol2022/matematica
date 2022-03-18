from time import sleep

# TODO
#########################################

def escala_real(MDM, MDR):
    CCR = MDR / 100000
    sleep(1)
    print('{}/{} = {}/Distancia real'.format(MDM, MDR, CCR))
    sleep(1)
    print('Distancia real = {} x {}/{}'.format(CCR, MDR, MDM))
    DR = CCR * MDR
    DF = DR / 100000
    sleep(2)
    print('Distancia real = {} = {}'.format(DR, DF))
    sleep(2)
    print(f'Então 1cm do mapa corresponde a {DF}')

#Funçao principal do programa
def main():
    MDM = float(input('Medida da distancia do mapa: '))
    MDR = int(input('Medida da distancia real: '))
    escala_real(MDM, MDR)

if __name__ == '__main__':
    main()