#testcase:
s = "Here's a string!"

print(s)
#creating new string and concatenating as we loop through given string
def space_replace(s):
    new_str = ""

    for val in s:
        if val == " ":
            new_str = new_str + '%20';
        else:
            new_str = new_str + val;
    return new_str;

print(space_replace(s))

#in-place replacements with enumerate
def space_replace_enum(s):
    enum_list = list(enumerate(s));
    s = "";

    for index,char in enum_list:
        if char == " ":
            char = '%20';
        s = s + char;
    return s;

print(space_replace_enum(s))
