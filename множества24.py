my_set= {1, 2, 3, 4, 5, 1, 3, 2, 'String', (1, 2, 3)}
print(my_set)
set_=set(my_set)
print(set_)
set_.add(45)
set_.add(11)
print(my_set)
my_set.remove('String')
print(my_set)