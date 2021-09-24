# first item in a list
def first_item(my_list): return my_list[0]


first_item(['cat', 'dog', 'mouse'])

# mapping
names = ['Magda', 'Jose', 'Anne']

lengths = []
for name in names:
    lengths.append(len(name))

lengths = list(map(len, names))

lengthOfYourPP = sum(lengths) / len(lengths)

print(lengthOfYourPP)
