import itertools
import operator

def lt_2(n):
    if n < 2:
        return True
    return False

letters = ['a', 'b', 'c', 'd']
numbers = [1, 1, 2, 3, 2, 1, 0]
names = ['Corey', 'Nicole']

def get_state(person):
    return person['state']

people = [
    {
        'name': 'john doe', 'city': 'gohtam', 'state': 'NY'
    },
    {
        'name': 'hane ode', 'city': 'kings', 'state': 'nt'
    },
    {
        'name': 'han ode', 'city': 'gong', 'state': 'nt'
    },
    {
        'name': 'ki ode', 'city': 'kings', 'state': 'nt'
    }]

person_group = itertools.groupby(people, get_state)
for key, group in person_group:
    print(key, len(list(group)))
    for person in group:
        print(person)
    print()
    
copy1, copy2 = itertools.tee(person_group)

# result = itertools.accumulate(numbers, operator.mul)
# for item in result:
#     print(item)

# result = itertools.takewhile(lt_2, numbers)
# for item in result:
#     print(item)

# result = itertools.dropwhile(lt_2, numbers)
# for item in result:
#     print(item)

# result = itertools.filterfalse(lt_2, numbers)
# for item in result:
#     print(item)        

# result = filter(lt_2, numbers)
# for item in result:
#     print(item)

# selectors = [True, True, False, True]
# result = itertools.compress(letters, selectors)
# for item in result:
#     print(item)

# result = itertools.combinations(letters, 2)
# result = itertools.permutations(letters, 2)
# result = itertools.product(numbers, repeat=4)
# result = itertools.combinations_with_replacement(numbers, 4)
# for item in result:
#     print(item)

# combined = letters + numbers + names
# combined = itertools.chain(letters, numbers, names)
# for item in combined:
#     print(item)

# result = itertools.islice(range(10), 1, 5, 2)
# for item in result:
#     print(item)

# with open('test', 'r') as f:
#     header = itertools.islice(f, 3)
#     for line in header:
#         print(line, end='')

# counter = itertools.count(start=5, step=-2.5)

# data = [100, 200, 300, 400, 500]

# daily_data = list(zip(itertools.count(), data))

# daily_data = list(itertools.zip_longest(range(10), data))

# print(daily_data)

# counter = itertools.cycle(('on', 'off'))

# counter = itertools.repeat(2, times=3)

# squares = map(pow, range(10), itertools.repeat(2))
# print(list(squares))

# squares = itertools.starmap(pow, [(0, 2), (5, 2), (2, 2)])
# print(list(squares))



# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
