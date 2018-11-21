import re

print("calculator")
print("type quit to exit") # instructions

previous=0 #to store and reuse the previous value
run=True #to run the while loop

def calc(): #to define the function
    global run
    global previous #to access the value inside the function
    equation= ""
    if previous==0:
        equation=input("enter equation")
    else:
        equation=input(str(previous))
    if equation=='quit':
        run=False
    else:
        equation=re.sub("[a-zA-Z,./?<>@#$&]",'',equation) #to reject the unwanted things bcz it actually crashes
        if previous==0:
            previous=eval(equation) #evaluate the given equation
        else:
            previous=eval(str(previous) + equation) #evaluate the given eqn with previous equation

while run:
    calc() #call the function

#*********************************the end**************************************#
