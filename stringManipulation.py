def cipher(text):   # cifer function
    spaces = [] # list to hold spaces
    for i in range(len(text)):  # loop through text
        if text[i] == " ":  # checks if current char is a space
            spaces.append(i)    # store space position
    text = text.replace(" ", "").upper()    # remove spaces + make uppercase
    return text, spaces # return ciphered text + where spaces are

def decipher(text, spaces): # decipher function
    text = text.lower() # make lowercase
    for i in spaces:    # loop through space positions
        text = text[:i] + " " + text[i:]    # insert space in given position
    return text.capitalize()    # not sure if needed or if upper/lowercase has to be specified for each character but
# (continuation of previous comment: for this assignment i left it as capitalizing the first letter of the sentence)

message = "The world population is increasing rapidly"

ciphered, spaces = cipher(message)

print("ciphered message:", ciphered)

print("space positions:", spaces)

original_text = decipher(ciphered, spaces)

print("Deciphered:", original_text)

# github link: https://github.com/cmorcos/SSW540/blob/main/stringManipulation.py

