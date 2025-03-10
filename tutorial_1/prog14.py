# Program 14
fib_series = [0, 1]
for i in range(8):
    fib_series.append(fib_series[-1] + fib_series[-2])

print("First 10 Fibonacci numbers:", *fib_series)