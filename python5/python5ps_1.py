#!/usr/bin/env python3
#1. Write a script in which you constuct a dictionary of your favorite things. 
my_favorite_things = {'animal' : 'dog', 'hobby' : 'jewelry', 'food' : 'avocado', 'organism' : 'cat'}

# 2. Print out your favorite book. I did animal instead. 
print(my_favorite_things['animal'])

# 3. Print out your favorite book (animal instead) but use variable in the key. 
fav_thing = 'animal'
print(my_favorite_things['animal'])

# 4. Now print your favorite tree. I did food instead. 
print(my_favorite_things['food'])

# 5. Add your favorite 'organism' to the dictionary. Make organism the new key of fav_thing. 
fav_thing = 'organism'
print(my_favorite_things[fav_thing])

# 6. Use a for loop to print out each key and value of the dictionary. 
for favorite_thing in my_favorite_things:
     mft = my_favorite_things[favorite_thing]
     print(favorite_thing, mft)





