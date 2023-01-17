from random import randint
import time

lista = []
jogos = []
tot = 1

time_start = time.time()

while tot <= 100:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Cartela {i+1}: {l}')

time_end = time.time()
print(f'Runtime of program: {time_end - time_start} seconds')