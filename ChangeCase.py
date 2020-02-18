def swap_case(s):
    length = len(s)
    for i in range(length):
        # if s[i].islower():
        #     s[i].upper()
        # elif s[i].isupper():
        #     s[i].lower()
        if s[i].islower:
            s[i] = s[i].upper()
            print("LOWER")
        elif s[i].isupper():
            s[i] = s[i].lower()
            print("UPPER")

    return s

s = input()
# result = swap_case(s)
print(swap_case(s))
