def frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1  
    return dict(sorted(freq.items()))

# Example usage
text = "this is an example"
print(frequency(text))


