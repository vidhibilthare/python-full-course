# function returning function closure

def to_power(x):
    def clac_power(n):
        return n**x
    return clac_power
cube = to_power(3)
print(cube(5))

square = to_power(2)
print(square(5))