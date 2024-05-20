def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "Fizzbuzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    else:
        return num
print(fizz_buzz(45))