array_1=[1,22,41,56,12,11,9,18,10,121,88,100]
array_len=len(array_1)
for x in range(0,array_len-1):
    for i in range(0,array_len-x-1):
        if array_1[i] < array_1[i+1]:
            array_1[i],array_1[i + 1] = array_1[i + 1], array_1[i]
    print(x+1)
    print(array_1)
    

encount=0
print("Введите свое любимое число")
while True:
    num=input()
    if num.isdigit() is False:
        if encount<3:
            encount+=1
            print("Вводите числа!!!")
            continue
        elif encount<4:
            encount+=1
            print("Число или бан")
            continue
        elif encount<5:
            encount+=1
            print("LAST TRY")
            continue
        else:
            print("Exit with code 0 ahahahaah")
    else:
        print("SPS your num is  "+num)
    break

    
    

