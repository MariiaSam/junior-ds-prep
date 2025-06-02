# find = open('prometheus/7.2/example.txt')
# for line in find:
#     line = line.strip()
#     print(line)
    
'''
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
Lorem Ipsum when an unknown printer took a galley of type and scrambled it to make a type
specimen book. It has survived not only five centuries, but also the leap into
Lorem Ipsum electronic typesetting, remaining essentially unchanged. It was popularised in
the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
Lorem Ipsum and more recently with desktop publishing software like Aldus PageMaker including
versions of Lorem Ipsum.
'''
'''
find2 = open('prometheus/7.2/mbox.txt')

for line in find2:
    line = line.strip()
    print(line)

print(len(line)) # 75

'''

find2 = open('prometheus/7.2/mbox.txt')

count = 0

for line in find2:
    count = count + 1
    print(count)



