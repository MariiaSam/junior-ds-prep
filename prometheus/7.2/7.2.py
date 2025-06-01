'''
Напишіть програму, яка запитує ім'я файлу, потім відкриває цей файл і читає його, шукаючи рядки заданої форми:

X-DSPAM-Confidence:    0.8475

Підрахуйте кількість цих рядків і витягніть значення з рухомою крапкою з кожного такого рядка, обчисліть середнє арифметичне цих значень і виведіть результат, як показано нижче. Не використовуйте функцію sum() або змінну з іменем sum у своєму розв'язку.

Зразок даних можна завантажити за адресою. Під час тестування введіть mbox-short.txt як ім'я файлу.
'''


# Use the file name mbox-short.txt as the file name
f# Запитуємо ім'я файлу
fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

count = 0
total = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    # Витягуємо число після ':'
    colon_pos = line.find(":")
    number_str = line[colon_pos+1:].strip()
    number = float(number_str)

    # Додаємо до суми і рахуємо кількість
    total += number
    count += 1

# Обчислюємо і виводимо середнє
if count > 0:
    average = total / count
    print("Average spam confidence:", average)
else:
    print("No matching lines found.")
