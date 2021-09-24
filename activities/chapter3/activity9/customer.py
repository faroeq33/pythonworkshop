# it should print John Smith (California)
def format_customer(first_name, last_name, location=''):
    if location != '':
        return first_name + " " + last_name + " (" + location + ")"
    return first_name + " " + last_name


john = format_customer("John", "Smith", "California")

print(john)
