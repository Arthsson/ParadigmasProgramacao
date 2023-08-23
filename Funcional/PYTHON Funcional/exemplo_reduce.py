'''exxemplo usando reduce (produto dos numeros)'''
from functools import reduce

print(reduce(lambda x,y: x*y,[1,2,3,4,5]))