
# Ek showNumbers() naam ka function define kijiye jo ki ek limit naam ka parameter 
# lega aur 0 se limit tak ke beech ke sabhi even aur odd numbers ko label ke saath 
# print karega jaisa ki niche dikhaya gaya hai. For example :- Input:-


def shownumbers():
    i=0
    while i<10:
        if i%2==0:
            print(i,"even number")
        else:
            print(i,"odd number")
        i=i+1
shownumbers()

