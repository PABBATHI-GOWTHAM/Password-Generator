import random
import string

def generate_password(length):
    # Define the character set: lowercase, uppercase, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    while True:
        try:
            # Prompt the user to specify the desired length of the password
            length = int(input("Enter the desired length of the password: "))
            
            if length < 1:
                print("Length must be at least 1. Please try again.")
                continue
            
            # Generate the password
            password = generate_password(length)
            
            # Display the generated password
            print(f"Generated Password: {password}")
            
            break
            
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
