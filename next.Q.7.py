

# Question 7

# Ek function define karo jo ki input me 2 strings lega aur dono strings me se jiski length jyaada 
# hogi use print karega aur agar dono strings ki length equal hui to dono ko line by line print 
# karega . Hint :- use len() builtin function.. Input



def builtin(list):
    i=0
    b=0
    while i<len(list):
        if b<len(list[i]):
            b=len(list[i])
            k=list[i]
        i=i+1
    print(k)
list=("savita","usha","chhaya","poojarani")
builtin(list)


         












