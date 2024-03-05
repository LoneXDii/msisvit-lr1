a = ((7+1) * (3+2))
testfunc()
testfunc(a)
testfunc(1+1)
b = 2 + (3-4)
for char in text:

    if char == "(" and ((new_word == "" and last_word not in funcs) or new_word not in funcs):
        res += 1
    elif (char not in string.ascii_letters and char != '_') and new_word != "":
        last_word = new_word
        new_word = ""
    elif char != '\n':
        new_word += char