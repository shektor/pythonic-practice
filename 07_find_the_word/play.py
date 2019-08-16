
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
