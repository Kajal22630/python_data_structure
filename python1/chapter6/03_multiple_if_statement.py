a= int(input("Enter your age: "))

if(a%2 == 0):
    print("a is even")


if(a>=18):
    print("you are above the age of consent")

elif(a<0):
    print("you are entering an invalid age")
elif(a==0):
    print("you are entering 0")

else:

    print("you are not above the age of consent")    

print("end of program")