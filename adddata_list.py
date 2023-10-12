# some more methods to add data in our list 
# insert method
# how to join (concatenate) two lists
# extend method
# difference b/w append and extend ,method

# insert

fruits1 = ["apple","banana","mango"]
fruits1.insert(1, "rose")
# fruits1.insert(5, "rose")
print(fruits1)

fruits2 = ["grapes","orange"]
# fruits = fruits1+fruits2
# print(fruits)
fruits1.extend(fruits2)
print(fruits1)

fruits1.append(fruits2)
print(fruits1)
