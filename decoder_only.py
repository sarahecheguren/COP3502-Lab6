def decode(encoded_password):
    """This function decodes a password by moving each digit of the password down by three numbers."""
    decoded_pass_string = ""
    for index, num in enumerate(encoded_password):
        num_int = int(num)
        decoded_num_int = (num_int - 3) % 10
        decoded_pass_string += str(decoded_num_int)
    return decoded_pass_string

#option 2 

elif option == str(2):
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original is {decoded_password}\n")
