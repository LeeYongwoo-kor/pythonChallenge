alphabets = 'abcdefghijklmnopqrstuvwxyz'
def position_in_alphabets(tofind):
    for i in range(0,26):
        if tofind == alphabets[i]:
            position = i+1
            break
    return position
def decrypt(a):
    output = ''
    for i in range(0,len(a)):
        character = a[i]
        z = i+1
        y = position_in_alphabets(character)
        x = z+y-26
        if x>len(alphabets):
            x = x % len(alphabets)
        alpha = alphabets[x-1]
        output += alpha
    return output
print ()
print ("NOTE : Please enter just lowercase characters (no special characters) and no spaces")
print ()
given = input("Please enter the word to be decrypted : ")
output = decrypt(given)
print ()
print ("The word which is coded as ",given," is : ",output)