print("Hello, Prometheus!")

fruit = "apple"
index = 0

while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index += 1
    
    '''
    0 a
1 p
2 p
3 l
4 e
    '''
    
for letter in fruit:
    print(letter)    

'''a
p
p
l
e'''

print("/////////////////////")
 
word = "banana"
count = 0

for letter in word:
    if letter== "a":
        count +=1
print(count)

"""3"""

print('//////////////////////')

example = '   Explore 100+ colorful and stylish summer nail ideas!   '

example.lstrip()
''''Explore 100+ colorful and stylish summer nail ideas!   '''

example.rstrip()
'''   Explore 100+ colorful and stylish summer nail ideas!'''

example.strip()
'''Explore 100+ colorful and stylish summer nail ideas!'''

text = "X-DSPAM-Confidence: 0.8475"
a = text.find(':')
print(a)

b =text[a+1:]
print(b) 

value = float(b)
print(value)
# b = text[a+1 : a]
# print(b)

# float(b)
# print(b)

c = text.find('0')
print(c)

d = float(text[c:])
print(d)
print(type(d))


# ++++++++++++++++++++==

a = {'b': 1, 'c': 2, 'd': 3}

new_dict = a.get('b', 0) + 1
print(new_dict)