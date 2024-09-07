logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

alphabets= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']


#METHOD-1(long)
'''def encrypt(text_message, shift_amount):
        cipher_text= ""
        for letter in text_message:
            position=alphabets.index(letter)
            new_position = position + shift_amount
            new_letter = alphabets[new_position]
            cipher_text += new_letter
        print(f"The encoded text is {cipher_text}")

    def decrypt(cipher_text,shift_amount):
        plain_text= ""
        for letter in cipher_text:
            position= alphabets.index(letter)
            new_position= position - shift_amount
            plain_text+= alphabets[new_position]
        print("The decode text is {plaini_text}")   


    if direction == "encode":
        encrypt(text_message=message, shift_amount=shift)

    elif direction== "decode":
        decrypt(cipher_text=message,shift_amount=shift)  '''  
#METHOD-2(short)


def ceaser(start_text,shift_amount,ceaser_direction):
        end_text=""
        if ceaser_direction=="decode":
            shift_amount *= -1

        for letter in start_text:
         position=alphabets.index(letter)
         new_position = position + shift_amount
         end_text += alphabets[new_position]

        print(f"Here is the {direction} result: {end_text}")  

should_complete=True
while should_complete:
    direction= input("Type 'encode' to Encrypt and 'decode' to Decrypt :\n")
    message= input("Type your message here: \n").lower()
    shift= int(input("How much shift you want: \n"))

    #Shift as much as you want
    shift = shift % 26

    ceaser(start_text=message,shift_amount=shift,ceaser_direction=direction)    

    restart=input("Type 'yes' if you want to go again otherwise type 'no'. \n")
    if restart== 'no':
        should_complete = False
        print("Goodbye")


        
