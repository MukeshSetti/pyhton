def prime_check(num):
    for i in range(2,int(num ** 0.5) + 1):
        if num % i == 0 :
            return False
    return True

def print_primes(mini , maxi):
    for i in range(mini , maxi + 1):
        if prime_check(i):
            print(i , end = ',')

mini = int(input('Enter a number to start printing primes from : '))
maxi = int(input('Enter a number where you want to end printing primes : '))
print_primes(mini , maxi)
