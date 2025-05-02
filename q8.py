def convert(s):
    words = s.split()
    unique = set(words)
    sorted = sorted(unique)
    return " ".join(sorted)
s = input("Enter your string:")
print(convert(s))