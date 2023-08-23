'''exemplos do uso do map (calculo de variancia)'''

print ((lambda x, f=lambda
x:sum(x)/float(len(x)),g=lambda x,z:map(lambda
y:y-z,x),h=lambda x:map(lambda y:y**2,x)
:sum(h(g(x,f(x))))/float(len(x)) ) ([1,4,3,7,9]))
