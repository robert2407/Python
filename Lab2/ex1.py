#   1. Write a function to return a list of the first n numbers in the Fibonacci string.

def fibonacci(n):
    fibo_vect = []
    a = 0
    b = 1
    for i in range(n):
        fibo_vect.append(a)
        temp = a
        a = b
        b = temp + b
    return fibo_vect

if __name__ == "__main__":
    n = int(input("Cate elemente sa aiba secventa: "))
    result = fibonacci(n)
    print(result)
