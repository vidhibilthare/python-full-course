name,char = input("enter your name and char").split(",")
print(f"length of your name is {len(name)}")
print(f"charecter count {name.strip().lower().count(char.strip().lower())}")#case sensitive


 #" Harshit  "----->"Harshit"---->"harshit"
 #" H  "---->"H"----->"h"
name.strip().lower().count(char.strip().lower())
# char.strip().lower()


