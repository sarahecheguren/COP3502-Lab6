def print_menu():
    print("""Menu
-------------
1. Encode
2. Decode
3. Quit\n""")

def encode(password_string):
    """This function encodes a password by moving each digit of the password up by three numbers."""
    encoded_pass_string = ""
    for index, num in enumerate(password_string):
        num_int = int(num)
        encoded_num_int = (num_int + 3) % 10
        encoded_pass_string += str(encoded_num_int)
    return encoded_pass_string

def decode(encoded_password):
    """This function decodes a password by moving each digit of the password down by three numbers."""
    decoded_pass_string = ""
    for index, num in enumerate(encoded_password):
        num_int = int(num)
        decoded_num_int = (num_int - 3) % 10
        decoded_pass_string += str(decoded_num_int)
    return decoded_pass_string

def main():
    run = True
    while run == True:
        print_menu()
        option = input("Please enter an option: ")
        if option == str(3):
            run = False
            break
        elif option == str(1):
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
            continue
        
if __name__ == "__main__":
    main()