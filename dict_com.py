# dictionaries comprehension
# square ={1:1,2:4,3:9}
# square ={f"Square of {num} is":num**2 for num in range(1,11)}
# # print(square)
# for k,v in square.items():
#     print(f"{k} : {v}")

string = "himanshu"
# {'h':2,'i':1,'m':1,'a':1,'n':1,'s':1,'h':2,'u':1}
word_count = {char:string.count(char) for char in string}
print(word_count)