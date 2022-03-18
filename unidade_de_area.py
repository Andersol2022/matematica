from time import sleep

#TODO
########################################
def unidade_de_area():
    principal = float(input('Digita um numero: '))
    sleep(1)
    print(f'''{principal}m2 = {principal / 10000000}km2
{principal}m2 = {principal / 1000000}hm2 
{principal}m2 = {principal / 10000}dam2
{principal}m2 = {principal}m2''')

#funcao principal do nosso programa
def main():
    unidade_de_area()

if __name__ == '__main__':
    main()