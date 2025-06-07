'''
10.2 Напишіть програму, яка прочитає файл mbox-short.txt і 
визначить розподіл по годинах доби для кожного з повідомлень. 

Ви можете витягнути годину з рядка 'From ', знайшовши час і розділивши рядок вдруге двокрапкою.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Після того, як ви накопичили кількість повідомлень для кожної години, виведіть їх, відсортовані за годинами, як показано нижче (у бажаному результаті).
'''
# import re

# fname = input('Enter the file name: ')
# try:
#     fn = open(fname)
# except:
#     print('File can not be opened', fname)
#     quit() 


# hours_count = dict()

# pattern = r'^From .*\s(\d{2}):\d{2}:\d{2}'


# for line in fn:
#     line = line.strip()
#     match = re.search(pattern, line)
#     if match:
#         hour = match.group(1)
#         hours_count[hour] = hours_count.get(hour, 0) + 1
        
 
# for hour in sorted(hours_count):
#     print(hour, hours_count[hour])
    
    
    
# ======================================

fname = input('Enter the file name: ')
try:
    fhandle = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

counts = dict()

for line in fhandle:
    line = line.strip()
    if line.startswith('From '): 
        parts = line.split()
        if len(parts) >= 6:
            time = parts[5] 
            hour = time.split(':')[0]  
            counts[hour] = counts.get(hour, 0) + 1

for hour in sorted(counts):
    print(hour, counts[hour])