#this is comment for this code
#this is diffrent comment
import random
c=random.randint(1,100)
k=0
g=0
while g!=c:

    print('guess the number until you are correct')
    print ("so now guess the number.. ")
    g = int(input("guess the number"))
    if  1<=g<=100  :
        pass

    else :
        print("OUT OF THE BOUNDS")
        k=k+1
        continue
    if g<c:
        print("warmer")
        k=k+1
        continue
    elif g>c:
        print ("colder")
        k=k+1
        continue
print("you gussed it correctly and you gussed it by attempting {} times ".format(k+1))
