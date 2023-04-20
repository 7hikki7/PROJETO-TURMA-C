from pack.bib import *
while(True):
    print("escolha qual exercício quer ver a resposta")
    exer= [1, 2 , 3, 4, 5, 6, 7]
    print(exer)
    resp= int(input("qual exercicio?"))
    if resp == 1:
        print("coloque quantos metros você quer saber em centimetros")
        metros= float(input("seus metros aqui >>"))
        ex1(metros)
        print(metros)
    elif resp == 2:
        pass
    elif resp == 3:
        pass
    elif resp == 4:
        pass
    elif resp == 5:
        pass
    elif resp == 6:
        pass
    elif resp == 7:
        pass
    else:
        break
print("numero inválido")