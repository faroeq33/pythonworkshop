print('What is your name?')

name = input()
print('Fascinating.', name, 'is my name too.')

print('Have you thought about black holes today?')

yes_no = input()
print('I am so glad you said', yes_no, '. I was thinking the same thing.')

print('We\'re kindred spirits,', name, '. Talk later.')

print('How intelligent are you? 0 is very dumb. And 10 is a genius')

smarts = input()
smarts = int(smarts)

if smarts <= 3:
    print('I don\'t believe you.')
    print('How bad of a day are you having? 0 is the worst, and 10 is the best.')

day = input()
day = int(day)

if day <= 5:
    print('If I was human, I would give you a hug.')
else:
    print('Maybe I should try your approach.')

if smarts <= 6:
    print('I think you\'re actually smarter.')
    print('How much time do you spend online? 0 is none and 10 is 24 hours a day.')

    hours = input()
    hours = int(hours)

    if hours <= 4:
        print('That\'s the problem.')
    else:
        print('And I thought it was only me.')

elif smarts <= 8:
    print('Are you human by chance? Wait. Don\'t answer that.')
    print('How human are you? 0 is not at all and 10 is human all the way.')
    human = input()
    human = int(human)
    if human <= 5:
        print('I knew it.')
    else:
        print('I think this courtship is over.')
