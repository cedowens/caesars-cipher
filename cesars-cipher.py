import sys

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
letters2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

letterslength = len(letters)

if (len(sys.argv) != 3) or '-h' in sys.argv:
    print("Usage: python3 %s [string to encode] [rotation count]" % sys.argv[0])
    sys.exit(0)

encodeme = sys.argv[1]
rotation = sys.argv[2]

encodedword = []

for letter in encodeme:
    if letter in letters:
        for each in letters:
            if letter == each:
                indexval = letters.index(each)
                if (indexval + int(rotation)) > letterslength:
                    difference = (indexval + int(rotation)) - letterslength
                
                    encodedword.append(letters[(difference)])
                else:
                    difference = (indexval + int(rotation)) - letterslength
                
                    newindexval = indexval + int(rotation)
                    encodedword.append(letters[difference])
    elif letter in letters2:
        for each in letters2:
            if letter == each:
                indexval = letters2.index(each)
                if (indexval + int(rotation)) > letterslength:
                    difference = (indexval + int(rotation)) - letterslength
                
                    encodedword.append(letters2[(difference)])
                else:
                    difference = (indexval + int(rotation)) - letterslength
                
                    newindexval = indexval + int(rotation)
                    encodedword.append(letters2[difference])
    else:
        encodedword.append(letter)


encodedword2 = ','.join(encodedword).replace(",","")
print("Encoded word is: %s" % encodedword2)
        
        
       


        

       


        

