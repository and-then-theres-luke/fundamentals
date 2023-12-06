students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
newList = [] # not too bad
for i in students:
    newList.append(i["first_name"])

# list comprehension


#                           pass in a for loop here > then an if statement if you want
newList2 = [i["first_name"] for i in students if i["first_name"] == 'Michael'] # this is a little better

print(newList2)