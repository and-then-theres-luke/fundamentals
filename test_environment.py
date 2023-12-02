#4 Iterate Through a Dictionary with List Values
#Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

def printInfo(some_dictionary):
    for dic_count in dojo:
        x = str(dic_count).upper()
        print(len(some_dictionary[dic_count]), x)
        for list_count in some_dictionary[dic_count]:
            print(list_count)
        print(" ")



dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)