
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


print('1!={:,}, 3!={:,}, 5!={:,}, 10!={:,}'.format(
    factorial(1),
    factorial(3),
    factorial(5),
    factorial(10),
))


def fibonacci_co():
    current = 0
    next = 1

    while True:
        current, next = next, next + current
        yield current


for n in fibonacci_co():
    if n > 100:
        break

    print(n, end=', ')
