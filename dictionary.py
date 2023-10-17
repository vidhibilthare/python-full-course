# dictionary
# why we use dictionary..?
# beacuse of limitations of lists,listsare not enough to
# represent real data

# # Example-
# user =["vidhi",26,['gadar','dash'],['dil','rock']]
#this list contains user name,age,fav movie,fav songs
# you can do this but this is not a good way to do this

# whts are dictionaries.?
# unordered collections of data in key:value pair.

# how to create a dictionary
# dictonaries no indexing
user = {'name':'Vidhi','age':26}
print(user)
print(type(user))

# second method to creating dictionaries
user1=dict(name="vidhi",age=26)
print(user1)
print(type(user1))

# how to access data from dictionary
# NOTE-:there is no indexing because of unordered collection of data.
print(user["name"])
print(user["age"])

# which type of data a dictonary can store.
# anything
# numbers,strings,lists,dictionary
user_info={
    'name ': "vidhi",
    'age' : 24,
    'color' : ['black','white'],
    'flower' : ['rose','lotues'],
}
print(user_info['flower'])


# how to add data empty dictionary

user_info2 = {}
user_info2['name']='vidhi'
user_info2['age']=26
print(user_info2)
