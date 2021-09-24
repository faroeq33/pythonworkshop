def add_suffix(suffix='.com'):
    return 'google' + suffix


defaultValue = add_suffix()
englishValue = add_suffix('.co.uk')

print(defaultValue)
print(englishValue)
