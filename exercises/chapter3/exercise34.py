# Dit is een voorbeeld bestand die je kan gebruiken om een script te runnen in de commandline
import math

numbers = [5, 7, 11]

# hoe kan het dat je een for loop in een array kan stoppen?
result = sum([math.factorial(n) for n in numbers])
print(result)
