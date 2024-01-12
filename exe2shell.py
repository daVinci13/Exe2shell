import sys

def read_file_in_chunks(file_location, chunk_size=8192):
    try:
        content = bytearray()
        with open(file_location, 'rb') as file:
            while (chunk := file.read(chunk_size)):
                content.extend(chunk)
        return content
    except:
        return None

def format_content(content):
    if content is not None:
        return '\\x' + '\\x'.join(format(byte, '02x') for byte in content)
    else:
        return None

def main():
    if len(sys.argv) != 2:
        print("Please provide a file name as an argument.")
        return
    file_location = sys.argv[1]
    content = read_file_in_chunks(file_location)
    formatted_content = format_content(content)
    if formatted_content is not None:
        print(formatted_content)

if __name__ == "__main__":
    main()
