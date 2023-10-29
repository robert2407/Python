# 7. Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements.
# The first element of the tuple will be the number of palindrome numbers found in the list and the second element
# will be the greatest palindrome number.

def palindr(number):
    if number < 0:
        return False

    copy_number = number
    palindrom_check = 0

    while number > 0:
        last_digit = number % 10
        palindrom_check = palindrom_check * 10 + last_digit
        number = number // 10

    return copy_number == palindrom_check

def find_all_palind(numbers):
    palindrome_count = 0
    max_palindrome = None

    for i in numbers:
        if palindr(i):
            palindrome_count += 1
            if max_palindrome is None or i > max_palindrome:
                max_palindrome = i

    return (palindrome_count, max_palindrome)

if __name__ == "__main__":
    numbers = [121, 123, 1331, 2442, 555, 98789, 10, 11]
    result = find_all_palind(numbers)
    print(result)