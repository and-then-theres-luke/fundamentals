# 1. TASK: print "Hello World"
print("Hello World!")
# 2. print "Hello Noelle!" with the name in a variable
name = "Luke"
print("Hello", name, "!")	# with a comma
print("Hello " + name + "!")	# with a +
# 3. print "Hello 42!" with the number in a variable
favorite_number = 7
print("Hello", favorite_number)	# with a comma
print("Hello " + str(favorite_number))	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
favorite_food1 = "ramen"
favorite_food2 = "pho"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print(f'''I love to eat {fave_food1} and {fave_food2}.''') # with an f string

