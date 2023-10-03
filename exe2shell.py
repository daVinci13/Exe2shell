# Function to read a file from a given location
def read_file(file_location):
    """
    This function reads a file from a given location and returns its content.
    :param file_location: The location of the file to be read.
    :return: The content of the file.
    """
    try:
        with open(file_location, 'rb') as file:
            content = bytearray(file.read())
        return content
    except FileNotFoundError:
        print("The file was not found.")
        return None
    except PermissionError:
        print("You do not have the permission to read the file.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to format the content of a file
def format_content(content):
    """
    This function formats the content of a file.
    :param content: The content of the file to be formatted.
    :return: The formatted content.
    """
    if content is not None:
        return '\\x' + '\\x'.join(format(byte, '02x') for byte in content)
    else:
        return None

# Main function
def main():
    """
    This is the main function that asks the user for the location of the file,
    reads the content of the file, formats the content of the file, and prints the formatted content.
    """
    # Ask the user for the location of the file
    file_location = input("Enter the file location: ")
    # Read the content of the file
    content = read_file(file_location)
    # Format the content of the file
    formatted_content = format_content(content)
    # Print the formatted content
    if formatted_content is not None:
        print(formatted_content)
    else:
        print("Could not format the content.")

# If this script is being run directly (not imported as a module), call the main function
if __name__ == "__main__":
    main()
