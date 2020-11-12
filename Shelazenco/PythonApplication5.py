data=open("users.txt","a+")

l="qwerty"
p=123
register_check=input("Проходили ли вы регистрацию    ")
if register_check==("yes"):
    login=input("Введите логин ")
    if login==l:
        password=int(input("Введите пароль"))
        if password==p:
            print("Вы вошли в систему")
    else:
          print("Неверный логин или пароль")
       
elif register_check==("no"):
    register_check2=input("Желаете ли пройти")
    if register_check2=="yes":
        users_login=input("Введите свой логин ")
        data.write(users_login)
        users_pas=input("Введите свой пароль ")
        data.write(users_pas)
        print("Привет    "+users_login)
    elif register_check2=="no":
        print("До свидания")
else:
    print("Неверный ответ вводите только 'yes' или 'no'")
   
data.close()





    
