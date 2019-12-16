# use a generator to create the fibonacci sequence

def fib(num):
    a = 0
    b = 1
    for i in range(num + 1):
        yield a
        temp = a
        a = b
        b = temp + b


if __name__ == '__main__':
    while True:
        try:
            print(list(fib(int(input('Fibonacci sequence up to: ')))))
            break
        except ValueError:
            print('Please enter a number')
