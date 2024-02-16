# HW.4 Caesar Cipher
In today's digital age, keeping information secure is crucial. You've been tasked by a mysterious cyber security company to create a simple encryption tool called the Caesar Cipher. 
This tool will help encrypt messages to ensure their safety during transmission and also provide a way to decrypt them.

<br/>

## Overview of the Program
Caesar Cipher works by shifting each letter of the message by a certain number of positions in the alphabet. The shift number determines how the encryption and decryption is performed.

<br/>

## Functions Explained
The main function in this application is `caesar(text, shift, direction)`, which takes three parameters:

- Parameters:
   - `text`: The message to be encrypted or decrypted.
   - `shift`: The number of positions to shift the characters in the message.
   - `direction`: Whether to encrypt or decrypt the message (E for encryption, D for decryption).

- Returns:
     - `str`: The resulting string after encryption or decryption.

- Example:
     - `caesar("hello", 20, "e")` returns `"byffi"`
     - `caesar("byffi", 20, "d")` returns `"hello"`
  
- Note:
     - The shift number must be a positive whole number.
     - Any shift number greater than 25 is not supported.
     - If the provided shift number is less than 0 or higher than 25, it should return: **"invalid shift"**
     - If an invalid operation letter is provided, it should return: **"invalid option"**
  
<br/>

## Hint
- Try using `str.lower()`, `str.isalpha()`, `str.isdigit()` to manipulate your input.
  
<br/>

## Reminders
1. Implement error handling to gracefully handle invalid inputs and provide meaningful error messages to the user.
2. Design the application with a user-friendly interface to enhance the user experience and provide clear instructions and prompts to guide the user through the process.
3. Allow users to repeat the encryption or decryption process after it has ended without exiting the program.
4. Remember to add comments to explain your code and remove unused comments to keep your code clean.
  
<br/>

## Expected Output
![image](https://github.com/AUPP-CS/homework_4/assets/80062829/d170cf62-d418-4477-8fd5-4b0ef56dbfa3)
