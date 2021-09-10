firstDivisor = 24
secondDivisor = 36

counting = True
i = 1

while counting:
    # Is de teller deelbaar door 24 en 36? geef weer wat de LCM is
    if i % firstDivisor == 0 and i % secondDivisor == 0:
        print('The Least Common Multiple of', firstDivisor,
              'and', secondDivisor, 'is', i, '.')
        break
    i += 1
