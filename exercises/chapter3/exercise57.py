nums = list(range(1000))

filtered = filter(lambda x: x % 3 == 0 or x % 7 == 0, nums)

print(sum(filtered))

names = ['Ming', 'Jennifer', 'Andrew', 'Boris']
sorted(names, key=lambda x: len(x))

print(names)
