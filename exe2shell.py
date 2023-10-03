def read_file(file_location):
    with open(file_location, 'rb') as file:
        content = bytearray(file.read())
    return content

def format_content(content):
    formatted_content = '\\x' + '\\x'.join(format(byte, '02x') for byte in content)
    return formatted_content

def main():
    file_location = input("Enter the file location: ")
    content = read_file(file_location)
    formatted_content = format_content(content)
    print(formatted_content)

if __name__ == "__main__":
    main()
