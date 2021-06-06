def countdown(num):
    print(num)
    # Base Case
    if num <= 0:
        return
    else:
        countdown(num - 1)


# print(countdown(10))


def factorial(num):
    if num <= 0:
        return 1
    else:
        return num * factorial(num - 1)


# print(factorial(4))


def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)


# print(power(4, 2))


def product_of_array(nums, product=1):
    if len(nums) == 0:
        return product
    else:
        return product_of_array(nums[1:], product * nums[0])


# print(product_of_array([1, 2, 3, 10]))


def recursiveRange(n, sum=0):
    if n == 0:
        return sum
    else:
        return recursiveRange(n - 1, sum + n)


# print(recursiveRange(10))


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# end

# print(fib(10))
