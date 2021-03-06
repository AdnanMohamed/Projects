"""
Enter a number (N) and the program will generate all prime numbers up to that number.
This program uses The Sieve of Eratosthenes algorithm.
"""

if __name__ == '__main__':
    n = int(raw_input()) + 1

    x = [True for i in range(0, n)] # initiates the array of flags

    x[0] = False # 0 is not a prime number
    x[1] = False # 1 is not a prime number too

    for i in range(2, n):
        if(x[i]):
            y = i * 2

            # For every y multiples of i, y is not a prime number
            while y < n:
                x[y] = False
                y += i

            print i