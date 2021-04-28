# questiong 1 a

fib_n = 0
fib_n1 = 1
fib_printed = "" + str(fib_n) + " " + str(fib_n1)

for i in range(20):
    fib_n2 = fib_n + fib_n1
    fib_printed += " " + str(fib_n2)
    fib_n = fib_n1
    fib_n1 = fib_n2
print(fib_printed)

# question 1b
n = 2000
fib_n = 0
fib_n1 = 1
fib_n2 = 1
count = 2
fib_printed = "" + str(fib_n) + " " + str(fib_n1)

while fib_n2 < 2000:
    fib_n2 = fib_n + fib_n1
    count += 1
    fib_printed += " " + str(fib_n2)
    fib_n = fib_n1
    fib_n1 = fib_n2
    if fib_n2 > 2000:
        break
print(fib_printed)
print(count)

