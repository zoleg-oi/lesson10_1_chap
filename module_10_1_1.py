# Потоковая запись в файлы
import threading
import datetime
import time


# import pytz

def write_words(word_count, file_name):
    file = open(file_name, 'w', encoding='UTF-8')
    for i in range(word_count):
        file.write(f'Какое-то слово № {i + 1}\n')
        time.sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')


start = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
finish = time.time()

t = datetime.datetime.fromtimestamp(finish - start, datetime.timezone.utc).strftime('%#H:%M:%S.%f')
# получение зоны с помощью pytz
# t = datetime.datetime.fromtimestamp(finish - start, tz=pytz.timezone('Etc/GMT')).strftime('%#H:%M:%S.%f')

print(f'Работа потоков {t}')

start = time.time()
thread5 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread6 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread7 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread8 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread5.join()
thread6.join()
thread7.join()
thread8.join()
finish = time.time()

t = datetime.datetime.fromtimestamp(finish - start, datetime.timezone.utc).strftime('%#H:%M:%S.%f')
# получение зоны с помощью pytz
# t = datetime.datetime.fromtimestamp(finish - start, tz=pytz.timezone('Etc/GMT')).strftime('%#H:%M:%S.%f')

print(f'Работа потоков {t}')

# разделяем на потоки
# write_words(10, 'example5.txt')
# rite_words(30, 'example6.txt')
# write_words(200, 'example7.txt')
# write_words(100, 'example8.txt')
