with open ('books/frankenstein.txt') as f:
    file_contents = f.read()

print(file_contents[:300])

words = file_contents.split()

print(len(words))

def count_letters(string):
    d = dict()
    for char in string:
        char = char.lower()
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    return d

def display_letters(d):
    """
    take a dictionary of character occurances
    filter it to alpha characters only
    sort it
    print "the 'x' character was found xxxx times" for each character"""
    d2 = dict()
    for key in d.keys():
        if key.isalpha():
            d2[key] = d[key]
    t = []
    for key, value in d2.items():
        t.append((value, key))
    t.sort(reverse=True)
    for tup in t:
        print(f"the '{tup[1]}' character was found {tup[0]} times")

print(count_letters(file_contents))
print()
display_letters(count_letters(file_contents))