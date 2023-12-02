num1 = 42 #data type, primitive, number, variable declaration
num2 = 2.3 #data type, primitive, number, variable declaration
boolean = True #data type, primitive, boolean, variable declaration
string = 'Hello World' ##data type, primitive, string, variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #data type, composite, list, variable declaration
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #data type, composite, dictionary, variable declaration
fruit = ('blueberry', 'strawberry', 'banana') #data type, composite, tuple, variable declaration
print(type(fruit)) #log statement, access value
print(pizza_toppings[1]) #log statement, access value
pizza_toppings.append('Mushrooms') #add value
print(person['name']) # access value, log statement
person['name'] = 'George' #dictionary, change value
person['eye_color'] = 'blue' #dictionary, add value
print(fruit[2]) #access value, log statement

if num1 > 45: #conditional if statement start
    print("It's greater") #log statement
else: #conditional else statement continued
    print("It's lower") #log statement

if len(string) < 5: #conditional if statement start
    print("It's a short word!") #log statement
elif len(string) > 15: #conditional else if statment continued
    print("It's a long word!") #log statment
else: #conditional else statment continued
    print("Just right!") #log statment

for x in range(5): #for loop start
    print(x) # loop continues with x = 0 incrementing by one until condition in range is met (x >= 5)
for x in range(2,5): #for loop start
    print(x)# loop continues with x = 2 incrementing by one until condition in range is met (x >= 5)
for x in range(2,10,3): #for loop start
    print(x)# loop continues with x = 0 incrementing by 3 until condition in range is met (x >= 10)
x = 0 #changes value of x to 0
while(x < 5): #while loop start, comparison
    print(x) #logs statement about value of x
    x += 1 #increments by one and will continue until while comparison is valid

pizza_toppings.pop() #modifies list, takes the last value off the array
pizza_toppings.pop(1) #modifies list, takes off the second value in a list

print(person) #access value, log statement
person.pop('eye_color') #adds eye color to the person list
print(person) #this will print the same because eye color was not given a matching key pair. Or it will print the list with an undefined key pair

for topping in pizza_toppings: # for loop initialize, access values within list
    if topping == 'Pepperoni': #checks parameter of list value
        continue #returns to top of function, increments
    print('After 1st if statement') #log statement if parameter "Pepperoni" not met
    if topping == 'Olives': #checks parameters of list value
        break #exits loop if true

def print_hello_ten_times(): #defining a function
    for num in range(10): #initialize for loop, increments 10 times then stops
        print('Hello') # log statement

print_hello_ten_times() #invoke function

def print_hello_x_times(x): #defining a function, passing in a value as an argument
    for num in range(x): ##initialize for loop, increments x times then stops
        print('Hello') #log statement

print_hello_x_times(4) #invokes function

def print_hello_x_or_ten_times(x = 10): #defining a function, initializing a value, defaults to 10 but will use whatever number is passed in as range argument
    for num in range(x):#initialize for loop, increments 10 or x times then stops
        print('Hello') #log statement

print_hello_x_or_ten_times() #invokes function
print_hello_x_or_ten_times(4) #invokes function 4 times


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)