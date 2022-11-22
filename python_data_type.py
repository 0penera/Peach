# work with string data

message = "Hello World"
message_2 = "Bobby's World"
name = "Corey"

# slice the string
print(message[2:6])
print(message[6:])

# string methods
print(message.lower())
print(message.upper())
print(message.count('Hello'))
print(message.find('World'))  
m1, m2 = message.split(' ')
print(m1, m2)
new_message = message.replace('World', 'Universe')
print(new_message)

# concatenate message
print(message + " " + name)
print('{} {} ! wellcome'.format(message, name))
print(f'{message} {name} ! wellcome')

# find help
# print(dir(name))
# print(help(str))

# ------------------------------------------------------

# working with int and float
num = 3
flo = 3.14

print(type(flo))
print(type(num))
print(3 // 2) #floor division
print(3 ** 2) #exponent
print(3 % 2) #modulus
print(3 * (2 + 1))
num += 1
print(num)
print(abs(-3))
print(round(3.75665, 2))
print(3 == 2)
print(3 != 2)
print(3 >= 2)
print(3 <= 2)
num_1 = '100'
num_2 = '200'
print(num_1 + num_2)
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)

