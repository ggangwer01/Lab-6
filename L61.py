#the authors name are Gwyn and Lily
x = 2
if x < 3:
    print("Small")


x = 5
if x < 3:
    print("Small")


score = 8 #A score on a 10 point quiz
if score > 6:
    print("Nice work!")


for i in range(1,16):
    if i % 3 == 0:
        print(i, " is divisible by 3.")


#number= int(input("Enter a number: "))
#if number % 2 ==0:
    #print("even")
#else:
    #print("odd")

x = 2
if x < 3:
    print("Small")
else:
    print("Large")
x = 5
if x < 3:
    print("Small")
else:
    print("Large")

score = 8 #A score on a 10 point quiz
if score < 6:
    print("Needs improvement")
elif score < 9:(
        print("Nice work!"))
else:
    print("Excellent!")



for i in range(-2,3):
    if i < 0:
        print(i, " is negative.")
    elif i == 0:
        print(i, " is zero.")
    else:
        print(i, " is positive.")


print(3 < 4)
print(4 > 2)
type(True)
if True:
    print("This text will always appear.")
if False:
    print("This text will not appear.")
type(False)
print(3 == 5)

def is_greater_than_10(number):
   return number > 10

print(is_greater_than_10(80))

#Working with Turtle Module

import turtle
riley= turtle.Turtle()
riley.width(5)
riley.speed(0)

def turtle_move(color):
    for side in range(5):
        riley.forward(100)
        riley.right(144)
        riley.color()

def main():
    mood=input("How are you feeling today?\n ")
    if mood =="angry":
        turtle_move("red")
    if mood== "sad":
        turtle_move("blue")
    if mood=="happy":
        turtle_move("pink")
    if mood== "sleepy":
        turtle_move("green")








