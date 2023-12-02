#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())

# Prediction: The console will log "5"
# Result: The console logged 5


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

# Prediction: This will give us an error. The first function isn't defined, so it can't return anything. But maybe that means it will just add "nothing." Either it will error, or just print 5
# Result: It was an error. If I wanted to get around this I could just write '''def number_of_days_in_a_week_silicon_or_triangle_sides(): pass ''' in the line above

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

# Prediction: This will print "5"
# Result: This printed "5"


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

# Prediction: This will print "5"
# Result: This printed "5"


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)

# Prediction: This will print 5 then print none since the function does not return anything
# Result: This will print 5 then print none

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))

# Prediction: The Console will print 3, 5, none
# Result: The Console will print 3, 5, and then gave an error. I guess they don't like adding things with no defined value.


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

# Prediction: This will print "25" as a string. 
# Result: This printed "25" as a string


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

# Prediction: This will print "100" then "10"
# Result: This printed "100" then "10"

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

# Prediction: This will print "7","14","21"
# Result: This printed "7","14","21"

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

# Prediction: This will print "8"
# Result: This printed "8"


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

# Prediction: This will print "500","500","300","500"
# Result: "500","500","300","500"

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

# Prediction: This is interesting. Can a function change a value of a global variable on return even if that value was not passed into the function? I will say yes. This will print "500","500","300","300"
# Result: Ok, lesson learned. The function can only affect the data of a global variable if that value is assigned to that variable when it is returned. This printed "500","500","300","500".

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

# Prediction: Based on what I learned from the last example, this should print "500","500","300","300" since this time the return of the function is assigned to a variable.
# Result: I was right, it was "500","500","300","300"



#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

# Prediction: The terminal will print "1","3","2"
# Result: "1","3","2"

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

# Prediction: The terminal will print "1","3","5","10"
# Result: "1","3","5","10"