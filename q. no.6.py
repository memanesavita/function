

# Question (Part 1)

# calculator naam ka ek function banao jo teen argument leta ho 
# - number_x, number_y, operation. number_x aur number_y mein hum 
# humesha do integers denge aur operation mein kaunsa operation karna hai woh denge.
#  Jaise: * Agar operation mein "add" diya toh number_x aur number_y ko add kar ke returna kareg


# def add_numbers(number_x, number_y):
#     number_sum = number_x + number_y
#     return number_sum

# sum1 = add_numbers(20, 40)
# print (sum1)
# sum2 = add_numbers(560, 23)
# a = 1234
# b = 12
# sum3 = add_numbers(a, b)
# print (sum2)
# print (sum3)
# number_a = add_numbers(20, 40) / add_numbers(5, 1)
# print (number_a) 


# def calculator():
#     num1=int(input("enter the num1"))
#     num2=int(input("enter the num2"))
#     symbol=(input("enter the symbole"))
#     if symbol=="+":
#         print(num1+num2)
#     elif symbol=="-":
#         print(num1-num2)
#     elif symbol=="*":
#         print(num1*num2)
#     elif symbol=="/":
#         print(num1/num2)
#     elif symbol=="%":
#         print(num1%num2)
#     elif symbol=="a**b":
#         print(num1**num2)
#     elif symbol=="a//b":
#         print(num1//num2)
#     else :
#         print(event)
# calculator()





# Question (Part 2)

# list_change naam ka ek function ka code likho jo 2 lists jisme integers arguments ki tarah le 
# aur fir unn lists ki woh items jo same index number (kram) pe hain unko multiply kar ke ek nayi 
# list return karvaye. Aapko multiply karne ke liye calculator function ka use karna hai. Normal 
# tareeke se multiply nahi kar sakte ho. Jaise agar hum function ko aise call karenge toh:
 
# multiple_list = list_change([5, 10, 50, 20], [2, 20, 3, 5]) 

# Yahan multiple_list ki yeh value honi chaiye:
 
# [10, 200, 150, 100] 

# 10, 5 aur 2 ko multiple kar ke aaya, 200 10 aur 20 ko multiple kar ke, 150 50 aur 3 ko, 100 20 aur 5 ko.





def list_chenge(list1,list2):
    i=0
    b=[]
    while i<len(list1):
        c=0
        while c<len(list2):
            x=list1[i]*list2[c]
            b.append(x)
            c=c+1
            i=i+1
    print(b)
list_chenge([5, 10, 50, 20], [2, 20, 3, 5])

