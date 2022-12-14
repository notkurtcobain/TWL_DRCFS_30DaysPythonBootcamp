
def add_one(num):
    result = num + 1
    print(result)

# add_one(5)


def greet(name):
    print("Hello," + name + "!")

# greet("Subodh")


def square(number):
    result = number * number 
    return result 
x = square(5)
z = x + square(10)
# print(z)

sq_x = square(5)
sq_y = square(6)
# print(sq_x + sq_y)


def cube(s):
    result = s * s * s
    return result 

x = cube(3)
y = cube(9)
z = x + y

# print('The value of x is', x)
# print('The value of y is', y)
# print('The required sum is', z)


def add(x,y):
    result = x + y
    return result 


add_result = add(2,3)
# print(add_result)


def greet(name: str) -> str:
    return  "Hi," + name + "!"
# print(greet("Kurt"))



