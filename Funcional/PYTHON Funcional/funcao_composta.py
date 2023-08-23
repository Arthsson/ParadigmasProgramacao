''''''

print((lambda x,f=lambda x,g=lambda x:3*x:g(x-1):f(x))(5))
print((lambda x: 3*(x-1))(5))

print((lambda x,g=lambda x,f=lambda x:3*x-x: f(x**x):g(x))(5))
print((lambda x: 3*(x**x)-(x**x))(5))


'''
    exemplificação básica 
    
    lambda parametro_1,parametro_2: funcao
    lambda parametro_3, parametro_funcao_1, parametro_funcao_2:funcao
    parametro_funcao_1 = lambda parametro_4,parametro_5: funcao
    parametro_funcao_2 = lambda parametro_6, parametro_funcao_3:funcao
    parametro_funcao_3 = lambda parametro_4,: funcao

'''