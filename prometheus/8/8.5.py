'''
Відкрийте файл mbox-short.txt і прочитайте його рядок за рядком.
Коли ви знайдете рядок, який починається з 'From ', як у цьому рядку:

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Ви маєте запарсити рядок From за допомогою методу split() і вивести друге слово у рядку (тобто повну адресу людини, яка надіслала повідомлення).

Потім виведіть кількість отриманих повідомлень.

Підказка: переконайтеся, що не включаєте рядки, які починаються з 'From:'. Також  подивіться на останній рядок прикладу даних, щоб дізнатися, як виводити кількість.


'''
fname = input('Enter file name: ')

try:
    fn = open(fname)
except:
    print('File can not opened', fname)
    quit()

count = 0

for line in fn:
    line = line.strip()
    if line.startswith('From '):
        words = line.split()
        if len(words) >= 2:
            print(words[1])
            count += 1

print("There were", count, "lines in the file with From as the first word")

            
        
        
        
        