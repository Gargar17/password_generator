# Password Generator Console Application

This Python script generates a random password based on user-defined preferences, including password length and the inclusion of symbols and/or numbers.

---

## Features
1. Generate a secure, random password.
2. Customize the password length.
3. Include or exclude symbols and numbers as per user preferences.
4. Simple and intuitive command-line interface.

---

## Prerequisites
- **Python 3.x** must be installed on your system.

---

## Setup Instructions
1. **Download the Script**  
   Save the code in a file named `password.py`.

2. **Open a Terminal or Command Prompt**  
   Navigate to the directory where the `password.py` file is located.

3. **Run the Script**  
   Execute the script by typing the following command:
   ```bash
   python password.py
   ```

---

## How to Use
1. **Welcome Screen**  
   Once the script runs, you'll see a welcome message:  
   ```
   Welcome to the Password Generator!
   ```

2. **Input Desired Password Length**  
   The program will prompt you to enter the desired password length:
   ```
   Enter the desired password length: 
   ```
   - Enter a number greater than or equal to 1.

3. **Choose to Include Symbols**  
   The program will ask if you want to include symbols:
   ```
   Include symbols? (y/n):
   ```
   - Type `y` for Yes to include symbols (e.g., `!@#$%^&*()`) or `n` for No.

4. **Choose to Include Numbers**  
   The program will ask if you want to include numbers:
   ```
   Include numbers? (y/n):
   ```
   - Type `y` for Yes to include numbers (e.g., `1234567890`) or `n` for No.

5. **View the Generated Password**  
   The program will generate and display the password based on your preferences:
   ```
   Generated Password: <YourPasswordHere>
   ```

---

## Example
### Input:
```
Enter the desired password length: 12
Include symbols? (y/n): y
Include numbers? (y/n): n
```

### Output:
```
Generated Password: aBc%De!Fg*Hi
```

---

## Notes
1. The script ensures that at least one type of character (letters, numbers, or symbols) is included in the password.
2. If no character type is selected, the program will notify you:
   ```
   You must include at least one character type (letters, numbers, or symbols).
   ```
3. If an invalid password length is entered, you'll see:
   ```
   Password length must be at least 1.
   ```

---

## Troubleshooting
1. **Python Not Found**  
   Ensure Python is correctly installed and added to your system's PATH.  
   Test by running:
   ```bash
   python --version
   ```

2. **ValueError**  
   If you input non-numeric characters for the password length, the program will prompt:
   ```
   Please enter a valid number for the password length.
   ```

---

Enjoy secure and customized password generation with this simple script! 😊