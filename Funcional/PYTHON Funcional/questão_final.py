'''
►Dê a forma funcional usando python das
seguintes funções
▪ y=x+1 sss 0<x<10, y=x**2+2x sss 10<=x<20 e
y=x**3 cc.
▪ f(x) = x-1 sss x<=2, f(x)=f(x-1)+1 cc
▪ Dados : f(x) =2X-1 e g(x)=x**2+2X. calcule
f(g(x)) para o intervalo [1,..,10]
'''

custom_function = lambda x: x + 1 if 0 < x < 10 else (x**2 + 2 * x if 10 <= x < 20 else x**3)

recursive_function = (lambda f: lambda x: x - 1 if x <= 2 else f(f)(x - 1) + 1)(lambda f: lambda x: x - 1 if x <= 2 else f(f)(x - 1) + 1)

f = (lambda x: 2 * x - 1)
g = (lambda x: x**2 + 2 * x)
composed_function = (lambda x: f(g(x)))


interval = range(1, 11)
results = list(map(lambda x: f(g(x)), interval))

print(results)

print(list(map(lambda x: (lambda x: 2 * x - 1)((lambda x: x**2 + 2 * x)(x)), range(1, 11))))
