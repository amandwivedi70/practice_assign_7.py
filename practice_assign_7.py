# question 1
month = int(input("enter your number"))
if month in (1,3,5,7,8,10,12):
    print ("31 days")
elif month in (4,6,9,11):
    print("30 days")
elif month==2:
    print("28 or 29 days")
else:
    print("invalid month number")

# question 2

print("1. addition")
print("2. substraction")
print("3. multiplication")
print("4. division")
choice=int(input())
match choice:
    case 1:
        print("enter two numbers")
        a,b=int(input()),int(input())
        c=a+b
        print(c)
    case 2:
        print("enter two numbers")
        a,b=int(input()),int(input())
        c=a-b
        print(c)
    case 3:
        print("enter two numbers")
        a,b=int(input()),int(input())
        c=a*b
        print(c)
    case 4:
        print("enter two numbers")
        a,b=int(input()),int(input())
        c=a/b
        print(c)
    
print()

# question 3
print("1. iosceles")
print("2. right angle")
print("3. equlateral triangle")
print("4. exit")
choice=int(input())
match choice:
    case 1:
        print("enter two numbers")
        a,b=int(input()),int(input())
        c= (a==b or a==c or b==c)
        print(c)
    case 2:
        print("enter two numbers")
        a,b=int(input()),int(input())
        c=a+b

        print(c/1.41)
    case 3:
        print("enter two numbers")
        a=int(input())
        c= 3*a
        print(c)
    case 4:
        exit()
    
print()

# question 4
print("enter your age")
age = int(input())
match age:
    case age if age<10:
        print('kid')
    
    case age if age<20: 
        print("teen")

    case age if age<40: 
        print("young")

    case age if age<60: 
        print("experienced")

    case age if age>=60:
        print("senior citizen")
print()

# question 5

print("enter your number")
number = int(input())
match number:
    case number if number%2==0:
        print('saurabh shukla')

    case number if number<0!=1:
        print('prateek jain')

    case number if number>0!=1:
        print('aditya choudhary')
print()

# question 6
print("enter a string")
string = (input())
match string:
    case string if " " not in string:
        print ("single word string")

    case string if " " in string:
        print ("multi word string")

print()

# queestion 7

print("enter your number")
number = int(input())
match number:
    case number if number>0:
        print('positive')

    case number if number<0:
        print('negative')

    case number if number==0:
        print('zero')
print()

# question 8

print("enter your string")
a1 = (input())
b = (input())
match (a1,b):
    case (a1,b) if a1>b:
        print ("{} then {}".format(a1,b))
        
    case (a1,b) if a1<b:
       print ( "{} then {}".format(b,a1))

print()

# question 9

print("enter your year")
year=(input())
match year:
    case year if year%400==0 or year%100!=0 and year%4 ==0:
        print("leap year")

    case year:
        print("not leap year")

print()

# question 10

print("yellow")
print("blue")
print("orange")
print("white")
print("black")
print("red")
print("all colours")
choice=(str.swapcase(input()))
match choice:
    case choice if choice==yellow:
        print("monday")

    case choice if choice==2:
        print("tuesday")

    case choice if choice==3:
        print("wednesday")

    case choice if choice==4:
        print("thursday")

    case choice if choice==5:
        print("friday")

    case choice if choice==6:
        print("saturday")

    case choice if choice==7:
        print("sunday")
print()