'''exemplo de filter (selecionando apenas impares e depois os pares)'''
nums = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x: x%2, nums)))

print(list(filter(lambda x: x%2==0, nums)))