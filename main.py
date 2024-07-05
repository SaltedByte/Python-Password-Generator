import random
import argparse

def main():
    #Process args 
    parser = argparse.ArgumentParser(description='Password Generator capable of creating passwords with unique requirements.')
    parser.add_argument('length', type=int, nargs='?', default=16, help='The length of the password (default: 16)')
    parser.add_argument('invalidChar', type=str, nargs='?', default="", help='List any characters that should not be included in the generated password.')
    args = parser.parse_args()
    
    #prepare the list of valid characters, removes any requested to be removed from args.
    validChar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    if args.invalidChar != "":
        for i in args.invalidChar:
            validChar.remove(i)
    random.shuffle(validChar)
    
    newPassword = ""
    #Generates the password from random characters left in the list of valid characters, then prints the result to the console.
    for i in range(args.length):
        newPassword += random.choice(validChar)
    print(newPassword)

if __name__ == "__main__":
    main()