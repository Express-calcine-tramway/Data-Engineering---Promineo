import json

us_trucks1 = {'make': 'Ford', 'model': 'F-150'}
us_trucks2 = {'make': 'Chevrolet', 'model': 'Silverado'}
us_trucks3 = {'make': 'Dodge', 'model': 'Ram 1500'}
us_trucks4 = {'make': 'Jeep', 'model': 'Gladiator'}

print(us_trucks2)
print(us_trucks3['make'])

# 7.     Create a list called, us_trucks_list, of the dictionaries you created in #1-4.
us_trucks_list = [us_trucks1, us_trucks2, us_trucks3, us_trucks4]

print(us_trucks_list)
print(us_trucks_list[1])

print(us_trucks_list[0]['model'])
print(us_trucks_list[0]['make'])
print(us_trucks_list[0]['model'])

# 13.  STRETCH: Find and print the element in the list where the truck is made by Chevrolet.
print(us_trucks_list[1])

# 14.  Print the element in the list where the truck is made by Jeep.
print(us_trucks_list[3])

# 15.  Parse the model of the truck made by Jeep from the list and print it to the console.
print(us_trucks_list[3]['model'])

# 16.  STRETCH: Try merging two of the four dictionaries together. You can do that a couple of ways,
# the dictionary update() function and a special Python trick, **. The update function syntax works like this:
# dict1.update(dict2) and the ** syntax works like this {**dict1, **dict2}. Try merging any two of the four dictionaries
# of us_truck and see what you get.  #Was the output what you expected? Did the update() function return 'None' and the
# ** trick only return the second dictionary? That's because a dictionary must have unique keys.
# Both dictionaries use the keys 'make' and 'model' so when you merge them the interpreter doesn't know how to reconcile
# the duplicate keys. Now try this:

dict1 = {'Dodge': 'Ram 150'}

dict2 = {'Ford': 'F-150'}

print(dict1)
print(20)
print(dict2)
dict1.update(dict2)
print(22)
print(dict1)
print(23)
print(dict2)

dict1 = {'Dodge': 'Ram 150'}
dict2 = {'Ford': 'F-150'}

#26.  {**dict1, **dict2} # With ** you don't change dict 1 or dict2, but if you want to see the result you need another variable

dict3 = {**dict1, **dict2}

print(28)
print(dict1)

print(29)
print(dict2)

print(30)
print(dict3)

# 31.  Next, read the 'new_families.txt' file (included in your course materials) into memory and assign the variable,
# file to the object.

file = open('new_families.txt', 'r')

# 32.  print(file) # Can you read the data in the file?
print(32)
print(file)
print('No, I cannot read the data in that file.')
# 33.  What is the datatype of the file variable? How can you read the data from the file variable?
print(33)
print(type(file))
print('No, I cannot read the data in that file.')

# 34.  Write a FOR loop to iterate over the Text IO object referenced by the file variable and print each iteration of the text.
# How many results did you get back? #HINT: you #should have only gotten one output.
print(34)
print("One gigantic dictionary-looking thing.")

# 35.  What is the datatype of the object returned in the iteration?
print(35)
print("It's a string.")


print(36)#.  Is it a string, a list, a dictionary? What happens when you try to parse the first item in the list?
    # #HINT: You should only get a single character because, even though, the data looks like a list of dictionaries, it's really a string.
print("Like I said, it's a string.")
# 37.  Next, change the string variable into a list of dictionaries type so you can work with it. #HINT: import json
print(37)
for f in file:
    json_in = f.replace("'",'"')
    new_f = json.loads(json_in)
# 38.  Now that you have a list, print only the second item from the list.
# What is its type? Now print only the value of the first element in the dictionary you parsed out from the list.
print(38)
print(new_f[1])
print(type(new_f[1]))
print(new_f[0])
# 39.
new_lst1 = [1, 2, 3]
new_lst2 = ['a', 'b', 'c']

# 41.  Join new_lst1 and new_lst2 together to make a new variable, new_lst3.
print(41)
new_list3 = new_lst1 + new_lst2
print(new_list3)