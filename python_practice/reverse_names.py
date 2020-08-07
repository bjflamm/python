
def reverse_names(first, last):
    return last + " " + first

first_name = raw_input("please enter your first name: ")
last_name = raw_input("please enter your last name: ")
print(reverse_names(first_name, last_name))