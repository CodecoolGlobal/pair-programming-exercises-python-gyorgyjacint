"""2. Modify the program as following:
   - for multiples of three, print "Fizz" instead of the number,
   - for the multiples of five, print "Buzz",
   - for numbers which are multiples of both three and five, print "FizzBuzz"."""

def fizzbuzz(number):
    
    if number % 15 == 0:
        return "FizzBuzz"
    if number % 5 == 0:
        return "Buzz"
    if number % 3 == 0:
        return "Fizz"
    else:
        return number
    


def main():
    fizzbuzz()
    return

if __name__ == '__main__':
    main()
