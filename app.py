import bcrypt

with open('bcryptlist.txt','r') as file:
    with open('wordlist.txt','r') as plain:
        data = file.readlines()
        text = plain.readlines()
        for i in data:
            result = i.rstrip('\n').encode('utf-8')
            for x in text:
                plaintext = x.rstrip('\n').encode('utf-8')
                if (bcrypt.checkpw(plaintext,result)):
                    print(f'{result} ---> [{plaintext}] (OK)')
                    break
    