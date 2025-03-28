#  WAP remove a given word from a list

def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    
    return n
    
l = ["Kajal", "Prachi", "Harshita", "hi"]

print(rem(l, "hi"))