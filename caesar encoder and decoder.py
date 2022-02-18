import string
letterslower = list(string.ascii_lowercase)
lettersupper = list(string.ascii_uppercase)
punctuations = list(string.punctuation)

# chooseindex function is meant to make letters from a-z to look
# circular so that after z comes a then so on
def chooseindex(n):
    if n>25:
        n = n-25-1
        return n
    elif n<0:
        n = 25+n+1
        return n
    return n

# this is to encode a message
# does so by adding n being the key to the index of a letter in the normal 
# alphabet and then find that index in letters
def caesarencode(text, n):
    
    # check ifthe key is between 0 and 26
    if (n > 26) or (n < 0):
        return "N must be shorter than 26 or greater or equal to 0"
    text = list(text) # text is changed into a list for easy
    for t in range(len(text)):
        
        #check if lower, check in lowercase values, else in uppercase
        if text[t].islower():
            letters = letterslower
        elif text[t].isupper():
            letters = lettersupper
            
        # if punctuation skip else choose letter at index + n
        # if index is out of range circulate using chooseindex function
        if not text[t] in punctuations and text[t] != ' ':
            text[t] = letters[chooseindex(letters.index(text[t])+n)]
    
    # reassemble the text
    temp = ""
    for t in text:
        temp+=t
    return temp


# this is to decode a message
# first create an alphabet list from n to 26 and append the letters before n
# on the back of the list
# then by adding the n on the index of each letters and replacing by the value 
# in the above list decodes the message
def caesardecode(text, n):
    
    # checks if the key is between 0 and 25
    if (n > 26) or (n < 0):
        return "N must be shorter than 26 or greater or equal to 0"
    text = list(text) # make the text into list for easy
    newletters = []
    for t in range(len(text)):
        
        # choose lowercase letters for lower otherwise uppercase letters list
        if text[t].islower():
            letters = letterslower
        elif text[t].isupper():
            letters = lettersupper
            
        # make the list from n to 26 then attach letters before n on the back
        # of the list
        newletters = letters[n:]
        newletters.extend(letters[:n])
        
        # skip if punctuation
        # if letter replace by letter at index + n in newletters
        # if out of range circulate using chooseindex
        if not text[t] in punctuations and text[t] != ' ':
            text[t] = newletters[chooseindex(newletters.index(text[t])-n)]
    
    # reassemble the text
    temp = ""
    for t in text:
        temp += t
    return temp
    
test = input("enter text to be encoded")
key = int(input("enter the key for encoding"))
encoded_message = caesarencode(test, key)

print("Encoded message:", encoded_message)
print("Decoded message:",caesardecode(encoded_message, key))
