'''
9.4 Напишіть програму, яка читає файл mbox-short.txt і з'ясовує, хто надіслав найбільшу кількість повідомлень.

Програма шукає рядки «From » і за другим словом цього рядка визначає особу, яка надіслала повідомлення. 

Програма створює словник Python, який зіставляє поштову адресу відправника з кількістю разів, коли вона з'являється у файлі. 

Після того, як словник створено, програма читає його, використовуючи цикл визначення максимального, щоб знайти найактивнішого дописувача.

'''

fname = input('Enter file name: ')
try:
    fn = open(fname)
except:
    print('File can not opened', fname)
    quit()

counts = dict()

for line in fn:
    line = line.strip()
    if not line.startswith('From: '):
        continue
    words = line.split()
    email = words[1]
    counts[email] = counts.get(email, 0) + 1
  
max_count = None
max_email = None

for email, count in counts.items():
    if max_count is None or count > max_count: 
        max_email = email
        max_count = count

print(max_email, max_count)


