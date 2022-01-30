# jmpicon

numeros = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
print(numeros)

def get_maximo(lst):
    return max(lst)

elem_maximos = list(map(get_maximo, numeros))

    

print('Maximun value', elem_maximos)



n = [x for x in [3, 4, 8, 5, 5, 22, 13] if x%2 == 0]

def es_primo(n):
    primo=True
    for i in range(2,n):
        if n%i==0:
            primo=False
    return primo 

num_primos = list(filter(es_primo, elem_maximos))

print('los primos son: ', num_primos)
print(n)