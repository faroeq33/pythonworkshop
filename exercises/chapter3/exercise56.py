import math

nums = [-3, -5, 1, 4]

lambafiedMap = map(lambda x: 1 / (1 + math.exp(-x)), nums)

answer = list(lambafiedMap)

print(answer)
