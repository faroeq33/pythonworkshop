over_18 = True

print(type(over_18))

over_21 = False

over_18, over_21 = True, False

print(over_18 and over_21)
print(over_18 or over_21)
print(not over_21 or (over_21 or over_18))
