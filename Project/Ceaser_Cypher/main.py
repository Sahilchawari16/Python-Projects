from logo import des
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print(des)
print("*********WELCOME TO THE ENCRYPTER************")

def encrypt(text,shift):
    encr = ""
    for i in range(0,len(text)):
        x = alphabet.index(text[i])
        find = x+shift
        if find >25:
            find = find-25
        encr += alphabet[find]
    return encr

def decrypt(text,shift):
    encr = ""
    for i in range(0,len(text)):
        x = alphabet.index(text[i])
        find = x-shift
        if find<0:
            find = find+25
        encr += alphabet[find]
    return encr


game = True

while game:
    way = input("Type 'encode' to encrypt or Type 'deocde' to decrypt \n").lower()
    text = input("Type message \n").lower()
    shift = int(input("Type shift number \n"))

    if way == 'encode':
      answer =  encrypt(text, shift)
      print(f"This is your Encrypted input {answer}")
      again =input("Do you Want start again ? Yes/No").lower()
      if again == 'no':
          game = False
    elif way == 'decode':
        answer = decrypt(text, shift)
        print(f"This is your Decrypted input {answer}")
        again =input("Do you Want start again ? Yes/No").lower()
        if again == 'no':
            game = False
    else:
        print("You have entered wrong input")