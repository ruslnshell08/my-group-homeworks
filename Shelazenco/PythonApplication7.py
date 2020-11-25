
def encrypt(file, key, file_ex):
    with open(file, "r") as encrypted_file:
        encrypted_file.seek(0)
        cp=encrypted_file.read()
        encrypted = ''.join(chr(ord(x) + key) for x in cp)
    with open (file_ex, "w") as decrypted:
        decrypted.write(encrypted)
    print("encrypted in file!")

def decrypted(file2,key2,file_ex1):
    with open(file2, "r") as d:
        d.seek(0)
        dcp=d.read()
        dcrypt = ''.join(chr(ord(x) - key) for x in dcp)
    with open (file_ex1, "w") as dcrypt:
        dcrypted.write(encrypted)
    print("decrypted  in file!")


check = int(input(" 1 = encrypt, 2 = decrypt"))
if check ==1:
    file=input("your file  ")
    key=int(input("your key  "))
    with open(file, "r") as encrypted_file:
        encrypted_file.seek(0)
        cp=encrypted_file.read()
        encrypted = ''.join(chr(ord(x) + key) for x in cp)
    file_ex=input("Enter name of encrypted file")
    encrypt(file,key,file_ex)

elif check==2:
    file_2=input("Enter your file")
    key_2=int(input("Enter your key"))
    with open(file2, "r") as d:
        d.seek(0)
        dcp=d.read()
        dcrypt = ''.join(chr(ord(x) - key) for x in dcp)
    decrypted_file=input("Enter name of decrypted file")
    decrypted(file_2,key_2,decrypted_file)
    
