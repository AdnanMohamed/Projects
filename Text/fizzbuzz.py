"""
This program will print the numbers from 1 to 100.
For multiples of three, the program will print "Fizz" instead of the number and "Buzz" if the number is multiples of five.
For multiples of both three and five, the program will print "FizzBuzz"
"""

if __name__ == '__main__':
    for i in range(1, 101):
        if(i % 3 == 0 and i % 5 == 0):
            print "FizzBuzz"
        elif(i % 5 == 0):
            print "Buzz"
        elif(i % 3 == 0):
            print "Fizz"
        else:
            print i
