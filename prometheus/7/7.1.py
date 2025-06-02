'''
7.1 Напишіть програму, яка запитує ім'я файлу, відкриває цей файл, читає його і виводить вміст файлу у верхньому регістрі. Використовуйте файл words.txt для виведення наведених даних.
'''

fname = input("Enter file name: ")
try:
    fn = open(fname)
    for line in fn:
        line = line.strip()
        print(line.upper())
        
except:
     print('File cannot be opened:', fname)
     quit()
