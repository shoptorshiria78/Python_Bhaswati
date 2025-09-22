my_tuple = ()

print(my_tuple)

my_tuple = (1, 2, 3)
print(my_tuple)

my_tuple = ("Hello", 1, 3.4)
print(my_tuple)

my_tuple = ([1, 2, 3], "mina", ("hello", "Hi", "Good morning"))
print(my_tuple)

my_tuple = ( 1, 5, 8, 12, 23)

print(my_tuple[3])

my_tuple = ([1, 2, 3], "mina", ("hello", "Hi", "Good morning"))

print(my_tuple[0][2])



sliced_tuple = my_tuple[1:2]
print(sliced_tuple)



my_tuple = ( 1, 5, 8, 12, 23)

for number in (my_tuple):
    print("Hello", number)