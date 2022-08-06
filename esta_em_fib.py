def esta_em_fib(x):
    sequencia = [0, 1]
    i = 2
    while True:
        sequencia.append(sequencia[i-1] + sequencia[i-2])
        if (sequencia[i]) >= x:
            return (x in sequencia)
        i += 1

print(esta_em_fib(34)) # True
print(esta_em_fib(35)) # False
