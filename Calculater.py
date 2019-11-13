#This Function for addition.
def add(x,y):
    return (x+y)

#This Function for substract.   
def sub(x,y):
    return (x-y)

#This Function for multiply.    
def mul(x,y):
    return (x*y)

#This Function for division.
def div(x,y):
    return (x/y)
    
    
#This line print opration list:-
#Chose your operater    
a = "1 = pluse(+)\n2 = substract(-)\n3 = multiply(*)\n4 = division(/)"
print(a)


#For Decoration
print(" ")
print("_"*40)
print(" ")


#Getting input from user
op = input()
x = int(input())
y = int(input())


#Logic in this program
if op == "1" or "+":
    print(x , "+" ,y ,"=",add(x,y))
elif op == "2" or "-":
    print(x , "-" ,y, "=",sub(x,y))
elif op == "3" or "*":
    print(x , "*" ,y ,"=",mul(x,y))
elif op == "4" or "/":
    print(x , "/" ,y ,"=",div(x,y))
else:
    print("you enterd wrong opration select between",a)


#For decoration
print(" ")
print("_"*40)
