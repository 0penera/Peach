courses = ['History', 'math', 'physics', 'compsci']
nums = [1, 2, 3, 4, 5]

#find value
print(courses.index('compsci'))
print('math' in courses)

#loop
for item in courses:
    print(item)
    
for index, item in enumerate(courses, start=1):
    print(index, item)
    
#list to sting and string to list
course_str = ', '.join(courses)
new_list = course_str.split(', ')
print(course_str)
print(new_list)

#adding value
courses_2 = ['health', 'education']
courses.extend(courses_2)
courses.append('art')
courses.insert(2, 'art')

#remove value
courses.remove('math')
poped = courses.pop()
print("poped : {}".format(poped))

#reverse
courses.reverse()

#sorting
courses.sort()
nums.sort(reverse=True)
sorted_courses = sorted(courses)


print(min(nums))
print(max(nums))
print(sum(nums))

print(courses)
print(len(courses))

#navigate value
print(courses[-1])
print(courses[0:3])


#tuple, immutable(not suupport item assignment)
tuple_1 = ('history', 'math', 'physics', 'compsci')
tuple_2 = tuple_1
print(tuple_2)
# tuple_1[0] = 'art'

#sets(remove duplicates and there no index order)
cs_courses = {'history', 'math', 'physics', 'compsci', 'math'}
art_courses = {'history', 'art', 'health', 'compsci', 'math'}
print(cs_courses)
print('math' in cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

