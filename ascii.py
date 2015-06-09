def ascii(letters):
    output = []
    for c in letters:
        output.append(ord(c))
    return output

def characters(numbers):
    output = ""
    for n in numbers:
        output += chr(n)
    return output

numbers = ascii("Paul Ryan Anderson")
original = characters(numbers)

print(numbers)
print(original)

