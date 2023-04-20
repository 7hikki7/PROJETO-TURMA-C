
def ler_metros():
    return float(input('Digite o valor em metros: '))


def metro_para_centimetros(x):
    return x * 100

def ex1():
    metros = ler_metros()
    cm = metro_para_centimetros(metros)
    print(f'{cm}cm')