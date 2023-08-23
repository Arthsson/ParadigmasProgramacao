'''
►Exemplos:
▪ Fazendo um teste com lambda :
►f(x) = x sss x<5
►f(x) = x^2 c/c
►print (lambda x: x < 5 and x or x**2)(10)

se x for meno que 5 mostre x se não mostre x ao quadrado

▪ Faça :
►Imprima todos os números pares de 1 a 100
'''

print((lambda x: x < 5 and x or x**2)(6))

print(list(filter(lambda x: x%2==0,range(1,101))))