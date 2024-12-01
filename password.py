import random
import string

def generate_password(length, include_symbols, include_numbers):
    if length < 1:
        print("Password length must be at least 1.")
        return None

    # Character pools
    letters = string.ascii_letters  
    digits = string.digits if include_numbers else ''  
    symbols = string.punctuation if include_symbols else ''  
    
   
    all_characters = letters + digits + symbols

    if not all_characters:
        print("You must include at least one character type (letters, numbers, or symbols).")
        return None
    
    # Generate password
    password = random.choices(all_characters, k=length)
    
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length: "))
        
        include_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
        include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        
        password = generate_password(length, include_symbols, include_numbers)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
