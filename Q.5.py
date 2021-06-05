

# Question 5

# on (Part 1)
# Yeh question 2 parts mein hai. Dono parts ka code 
# same file mein likh ke submit karein.


#  Questi
# check_numbers naam ka ek function likhiye jo do numbers le 
# aur fir print kare "Dono even hain" agar dono numbers even (2 se 
# divide hote hain) nahi toh print kare "Dono numbers even nahi hai"

# def check_numbers(a,b):
#     i=0
#     while i<1:
#         if a%2==0 and b%2==0:
#             print("dono even hain")
#         else:
#             print("dono no even nahi hai")
#         i=i+1
# check_numbers(10,10)
        





        # Question (Part 2)

# Ab ek check_numbers_list naam ka ek function likho jo inetgers ki list
# ko arguments ki tarah le aur fir check kare ki same index waale dono integers
# even hain ya nahi. Yeh check karne ke liye pichle Part 1 mein likhe check_numbers
# function ka use karo. Agar aapne apne function ko [2, 6, 18, 10, 3, 75] aur 
# [6, 19, 24, 12, 3, 87] Toh usko yeh output deni chaiye:


def check_function(a,b):
    i=0
    while i<len(a):
        if a[i]%2==0 or b[i]%2==0 :
            print(a[i],b[i],"dono even hai")
        else:
            print("dono even nahi hai")
        i=i+1
check_function([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])






