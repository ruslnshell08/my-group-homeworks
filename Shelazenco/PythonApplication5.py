p=123
l1="qwerty"
print("проходили ли ви регистрацию")
l=input()
if(l=="yes"):
    print("Введите свой пароль")
elif(l=="no"):
    print("Желаете пройти регистрацию")
    k=input()
    if(k=="yes"):
        print("Введите свой пароль")
        pp=input()
        print("Введите свой логин")
        ll=input()
    
    else:
        print("Досвидания!")



f=int(input())
print("Введите свой логин")
f2=input()

if p==f:
    if l1==f2:
        print("Вы вошли в систему!!!")
    else:
        print("Неверный логин или пароль")
else:
    print("Неверный логин или пароль")


aa=open("users.txt","w")
aa.write("                   ")
aa.close()
aa=open("users.txt","r")
print(aa.read())


    
