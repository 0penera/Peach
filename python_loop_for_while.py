nums = [1, 2, 3]

for num in nums:
    if num == 3:
        print('Found')
        continue #skip to the next iteration
        #break  stop iteration
    print(num)


for num in nums:
    for letter in 'ab':
        print(num, letter)
        
for i in range(1, 10, 3): #(start number, end number, size of step)
    print(i)
    
x = 0

while x < 5:
    if x == 3:
        break
    print(x)
    x += 1
    
while True:
    print(x)
    x += 1
