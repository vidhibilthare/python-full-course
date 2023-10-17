# add & delete data from dictionary
user_info={
    'name': "vidhi",
    'age' : 24,
    'color' : ['black','white'],
    'flower' : ['rose','lotues'],
}

# how to add data
user_info["song"]=["dil","love"]
print(user_info)

# pop methods
popped_item=user_info.pop('flower')
print(f"popped item is{popped_item}")
print(user_info)

# popitem methods
popped_item=user_info.popitem()
print(type(popped_item))
print(user_info)