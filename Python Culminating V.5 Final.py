#Still need a button that can exit the loop but doesn't interfere

while True:
    print("<Welcome to Edward's Text Encryptor, for all your text encrypting needs>")
    print("<Please select one of the 4 fine text encryptors for you to use>")
    print("> Type in the name to choose one of the following: <Morse_Code>, <Ceaser_Cipher>, <Atbash_Cipher>, <Baconian_Cipher>")
    choice = input(">")
    if  choice == "Morse_Code":
        def to_morse_code(text):
            code = {' ': '|', 'a': '. _', 'b': '_ . . .', 'c': '_ . _ .', 'd': '_ . .', 'e': '.', 'f': '. . _ .',           #Conversion dictionary
                    'g': '_ _.', 'h': '. . . .', 'i': '. .', 'j': '. _ _ _', 'k': '_ . _', 'l': '. _ . .', 'm': '_ _',
                    'n': '_ .', 'o': '_ _ _', 'p': '. _ _ .', 'q': '_ _ . _', 'r': '. _ .', 's': '. . .', 't': '_',
                    'u': '. . _', 'v': '. . . _', 'w': '. _ _', 'x': '_ . . _', 'y': '_ . _ _', 'z': '_ _ . .',
                    '1': '. _ _ _ _', '2': '. . _ _ _', '3': '. . . _ _', '4': '. . . . _', '5': '. . . . .',
                    '6': '_ . . . .', '7': '_ _ . . .', '8': '_ _ _ . .', '9': '_ _ _ _ .', '0': '_ _ _ _ _'}

            morse_code = '' # empty string to hold code during iteration

            for i in text:                      #function for translation
                morse_code += code[i.lower()]

            return morse_code

        text = (">Enter text to convert to Morse Code:")
        while True:
            #While loop to keep program running
            text = input(">Enter text to convert to Morse Code: ")
            print(to_morse_code(text))
            text = input(">Enter text to convert to Morse Code: ")
            i = input(">Enter to quit: ")
            if not i:
                break
            
    elif choice == "Ceaser_Cipher":
        def encrypt(text1,s):
            result = "" 
  
    # traverse text 
            for i in range(len(text1)): 
                char = text1[i] 
  
        # Encrypt uppercase characters 
                if (char.isupper()): 
                    result += chr((ord(char) + s-65) % 26 + 65) 
  
        # Encrypt lowercase characters 
                else: 
                    result += chr((ord(char) + s - 97) % 26 + 97) 
  
            return result 
  
        #check the above function
        text1 = input(">Enter your desired message:")
        s = 4
        print(encrypt(text1,s))
        while True:     #While loop to maintain
            text1 = input(">Enter your desired message:")    #Obtain function input
            print(encrypt(text1,s))          #Print function output
            text1 = input(">Enter your desired message:")                            #Exit from loop
            i = input(">Enter to quit:")
            if not i:
                break
    elif choice == "Atbash_Cipher":
        # Atbash Cipher 
        # Create an exit protocol for everything
        # Dictionary
        code = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V', 
            'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q', 
            'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L', 
            'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G', 
            'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'} 
  
        def atbash(message): 
            cipher = '' 
            for letter in message: 
        # checks for space 
                if(letter != ' '): 
            #adds the corresponding letter from the lookup_table 
                    cipher += code[letter] 
                else: 
                # adds space 
                    cipher += ' '
  
            return cipher 
  
            # Driver function to run the program 
        def main(): 
                #encrypt the given message 
            message = input(">Insert the message you wish the encrypt:")
            print(atbash(message.upper())) 
          
  
        message = input(">Insert the message you wish the encrypt:")
        print(atbash(message.upper()))  
        while True:
            main()
            i = input(">Enter to quit:")
            if not i:
                break                         #Exit thing
    


    elif choice == "Baconian_Cipher":
        code = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa', 
        'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab', 
        'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba', 
        'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb', 
        'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 'Z':'bbaab'} 
  
# Function to encrypt the string according to the cipher provided 
        def encrypt(message): 
            cipher = '' 
            for letter in message: 
        # checks for space 
                if(letter != ' '): 
            # adds the ciphertext corresponding to the  
            # plaintext from the dictionary 
                    cipher += code[letter] 
                else: 
            # adds space 
                    cipher += ' '
  
            return cipher 
  
# Function to decrypt the string  
# according to the cipher provided 

  
        def main(): 
            message = input(">Enter the message you wish to encrypt:")
            print(encrypt(message.upper()))
           
  

#Executes the main function
        message = input(">Enter the message you wish to encrypt:")
        print(encrypt(message.upper()))

        while True:
            main()
            i = input(">Enter to quit:")
            if not i:
                break

        
