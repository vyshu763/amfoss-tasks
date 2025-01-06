def frequency(s):
    
    frequencies = [0] * 10
    for char in s:
        if char.isdigit():
            digit = int(char)
            frequencies[digit] += 1

    return frequencies

s = input()
output = frequency(s)
print(" ".join(map(str, output)))

