# Swaping the numbers
x, y = 6,7
out = list(map(lambda x,y : (y,x), (x,), (y,)))     # Multiple returns will be tuple so we passed (y,x)
print(out)
[(x, y)] = out
print(x, end=' ')
print(y)

def func(x,y):
    x, y = y, x
    return x,y      # Multiple returns will be tuple
print(func(6,7))




students = [('Amanda','161cm','51kg'), ('Patricia','165cm','61kg'), ('Marcos','191cm', '101kg')]
students_height = list(map(lambda x:x[1], students))
print(students_height)

#list of strings
#students_height = ['161cm','165cm','191cm']

students_weight = list(map(lambda x:int(x[2][:-2]), students))
print(students_weight)



# input = 'Switch Words'
# l = input.split()
# print(l[0][:2])
# print(l[1][:2])
# output = []
# # result = l[0][:2] = l[1][7:9]
# # print(result)

# def func(l):
#     return l[0][:2] = l[1][:2]
    
# func(l)



# input : cda_t$_e
# output: acd_e$_t
import re

reg = "[^a-zA-Z0-9]+"
inp = "cda_adb_$ta"
matches = re.findall(reg, inp)
sorted_words = [
  ''.join(sorted(list(x))) for x in re.split(reg, inp)
]
result = [None]*(len(sorted_words)+ len(matches))

result[::2] = sorted_words
result[1::2] = matches

print(''.join(result))



# Example
o = [1, 2, 3, 4, 5]

r = [None]*(len(o))

s = [5, 4, 3, 2, 1]

print(r)
r[::-1] = o
print(r)

print(s)
s[:] = (1, 2, 3, 4, 5)
print(s)

o = [1, 3, 5]
e = [2, 4, 6]

r = [None]*(len(o)+len(e))

r[::2] = o
r[1::2] = e

print(r)
# a = 6 b= 7
# b= 6 a = 7

# Example to switch words
# "Switch words"
# "woitch swrds"

sample = "Switch words"
words = [list(word) for word in sample.split()]
print(words)

# temp = words[:]
# words[0][:2] = words[1][:2]
# words[1][:2] = temp[0][:2]

words[0][:2], words[1][:2] = words[1][:2], words[0][:2]
print(words)
result = ' '.join([''.join(elements) for elements in words])
print(result)

import profile
def swap_first_2_char_of_words(sample):
    words = [list(word) for word in sample.split()]

    # temp = words[:]
    # words[0][:2] = words[1][:2]
    # words[1][:2] = temp[0][:2]

    words[0][:2], words[1][:2] = words[1][:2], words[0][:2]
    result = ' '.join([''.join(elements) for elements in words])
    return result

print(swap_first_2_char_of_words('Prashant Jha'))
profile.run("print(swap_first_2_char_of_words('Prashant Jha'))")

array_of_integers = [1,2,3,3,4,4,3,2,344,4]
# largest = 0
def find_largest(array_of_integers):
    largest = 0
    for iteration in array_of_integers:
        if iteration > largest:
            largest = iteration
    return largest
print(find_largest(array_of_integers))

# from review import compute
from itertools import islice, tee
nwise = lambda g, n=2: zip(*(islice(g, i, None) for i, g in enumerate(tee(g, n))))
# windowed_avg = lambda g, n=2: (sum(xs) / len(xs) for xs in nwise(g, n))
print(list(nwise('abcdef')))

# def f():
#     while True:
#         yield compute()
# for x in windowed_avg(f(), 3):
#     print(x)