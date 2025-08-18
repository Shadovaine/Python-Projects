#-----------------------------------------
# Secure Password Generator (Annotated)
# Level 1 Project for Learning Python Structure.
#Logic, security libraries, and command-line tools.
#Author: Shadovaine
#--------------------------------------------

# IMPORTS
# argparse: handles command-line arguments like --length --symbols
# secrets: provides secure random generation (better than random)
# string: gives easy access to ascii letters, digits, and punctuation
# Says to import standard libraries
# import loads modules into memory so to be able to use the functions, classes, and variables. 
# These 3 modules are built-in to python, no need to install them with pip. 
import argparse, secrets, string # handles arguments,secure randomness, character sets

# FUNCTION: generate()
# - Purpose: returns a secure random password string
# - length:  specifies how many characters are to be in the password
# - use_symbols: specifies if special characters should be included
# gererates password of given length
def generate(length, use_symbols=False):
    # Directs to start with letters and digits
    chars = string.ascii_letters + string.digits
    
    # Add symbols if the user passed the --symbols flag
    if use_symbols:
        chars += string.punctuation

    # Generate the password using secure random choices    
    return ''.join(secrets.choice(chars) for _ in range(length))



# Sets up an argument parser
# - uses argparse to allow the user to customize the output
# - Example usage: python password_generator.py --length 20 --symbols
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate secure passwords.")
    parser.add_argument("--length", "-l", type=int, default=16)
    parser.add_argument("--count", "-n", type=int, default=1)
    parser.add_argument("--symbols", action="store_true")
   
    # Parse the arguments from the command-line into the 'args' object
    args = parser.parse_args()

# Prints the passwords
# MAIN SCRIPT EXECUTION
# - Loop 'args.count' times and prints each generated password
# - Uses the parsed args to determine settings
    for _ in range(args.count):
        print(generate(args.length, args.symbols))
