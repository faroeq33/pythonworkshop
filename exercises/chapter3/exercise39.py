list = [5, 8, 1, 3, 2]
still_swapping = True

while still_swapping:
    still_swapping = False
    for i in range(len(list) - 1):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
            still_swapping = True

print(list)
