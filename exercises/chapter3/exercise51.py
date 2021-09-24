def factorial_iterative(n):
    result = 1
    for i in range(n):
        result *= i + 1
    return result


print(factorial_iterative(5))


def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


# will have same output as previous function
print(factorial_recursive(5))
