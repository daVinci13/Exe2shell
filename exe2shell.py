fn = input("Enter the file location: ")

with open(fn, 'rb') as f:
    sc = bytearray(f.read())

print('\\x' + '\\x'.join(format(x, '02x') for x in sc))
