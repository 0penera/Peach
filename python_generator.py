'''generator dosen't hold the entire result in memory
it yield one result at a time 
this is waiting for the generate next result'''

# def square_numbers(nums):
#     for i in nums:
#         yield (i * i)

# # my_nums = square_numbers([1, 2, 3, 4, 5])

# my_nums = [x*x for x in [1, 2, 3, 4, 5]] # list
# my_nums = (x*x for x in [1, 2, 3, 4, 5]) # comprehensive generater explation

# print(list(my_nums)) #converting generator to list


# # print(next(my_nums))    
# # print(next(my_nums))
# # print(next(my_nums))
# # print(next(my_nums))
# # print(next(my_nums))
# # print(next(my_nums))

# for num in my_nums:
#     print(num)

#--------------------------------------------------------
# example   
'''comparing between generator and list 
    memory usage'''

import mem_profile
import random
import time

names = ['john', 'corey', 'adam', 'stive', 'rick', 'thomas']
majors = ['math', 'engineering', 'comsci', 'arts', 'business']

print('Memory (before): {}Mb'.format(mem_profile.memory_usage_resource()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
        }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
        }
        yield person

t1 = time.clock()
people = people_list(1000000)
t2 = time.clock()

t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()

print('Memory (after): {}Mb'.format(mem_profile.memory_usage_resource()))
print('took {} seconds'.format(t2-t1))

