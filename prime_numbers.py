def divisor(num):
    global x
    x = 0
    num_lst = []
    for digit in range(1, num + 1):
        if num % digit == 0:
            num_lst.append(digit)

    if len(num_lst) == 2:
        x = num_lst[1]
    return num_lst


primes = []


def prime(anum):
    for number in range(1, anum + 1):
        divisor(number)
        primes.append(x)
        for digit in primes:
            if digit == 0:
                primes.remove(digit)
    return primes


if __name__ == '__main__':
    while True:
        try:
            user_num = int(input('Enter a number to see primes up to that number: '))
            prime(user_num)

            print(primes)
            break
        except ValueError:
            print('please enter a number')
