#Function to read a file from a given location
def read_file(file_location):
    #Open the file in binary mode
    with open(file_location, 'rb') as file:
        #Read the content of the file into a bytearray
        content = bytearray(file.read())
    #Return the content of the file
    return content

#Function to format the content of a file
def format_content(content):
    #Format each byte of the content as a two-digit hexadecimal number,
    #join them together with '\\x' in between, and prepend '\\x' to the result
    formatted_content = '\\x' + '\\x'.join(format(byte, '02x') for byte in content)
    #Return the formatted content
    return formatted_content

#Main function
def main():
    #Ask the user for the location of the file
    file_location = input("Enter the file location: ")
    #Read the content of the file
    content = read_file(file_location)
    #Format the content of the file
    formatted_content = format_content(content)
    #Print the formatted content
    print(formatted_content)

#If this script is being run directly (not imported as a module), call the main function
if __name__ == "__main__":
    main()
