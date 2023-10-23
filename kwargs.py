# kwargs keyword argument
# **kwargs (double star operator)
# dictionary
# kwargs as a parameter
def func(**kwargs):
    # print(kwargs)
    for k , v in kwargs.items():
        print(f"{k}:{v}")
     

# func(first_name = 'vidhi' , last_name = 'shukla')
# dictionary unpacking
d={'name':'vidhi','age':26}
func(**d)
