''' soma de dois numeros mais o produto do mesmo
'''
print((lambda x,y,f=lambda x,y: x+y:f(x,y)+x*y)(3,2))
#      função=lambda(parametros x y f(função=lambda(corpo soma x+y)))função f


'''Funcionamento seria esse (f é um parametro que é uma função no caso)'''
def fuction1_x_y_f(x, y, f):
    return f+(x*y)

def function_f(x,y):
    return x+y

f = function_f(3,2)
print(fuction1_x_y_f(3,2, f))