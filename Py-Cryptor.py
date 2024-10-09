import base64

continue_process = True

def encrypt_pass(password):
    encrypted_pass = base64.b64encode(password.encode()).decode()
    with open("encrypted_password.txt", 'a') as pass_file:
        pass_file.write(f"{password} : {encrypted_pass}\n")
    print("The encrypted password is saved to encrypted_passwords.txt")

def decrypt_pass(base64_string):
    decrypted_string = base64.b64decode(base64_string.encode()).decode()
    with open("decrypted_passwords.txt", 'a') as dec_file:
        dec_file.write(f"{base64_string} : {decrypted_string}\n")
    print("The decrypted password is saved to decrypted_passwords.txt")


user_choice = input("Press 'E' for encryption and 'D' for decryption: ").capitalize()
if user_choice == 'E':
        user_pass = input("Enter your password: ")
        encrypt_pass(user_pass)
elif user_choice == 'D':
    try:
        user_str = input("Enter your encrypted string: ")
        decrypt_pass(user_str)
    except Exception as e:
        print(f"Enter a base64 encoded string - Error: {e}")
else:
    print("Invalid Input. Please enter 'E', 'D', or 'Q'.")
