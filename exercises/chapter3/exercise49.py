def is_prime(x):
    for i in range(2, x):
        if (x % i) == 0:
            return False
        return True


result = is_prime(7)
print(result)
