#Потоки в классах

import threading
import time

class knight(threading.Thread):
    '''
    Класс организует сражение рыцарей с врагами, для решения задачи
    организовано по потоку для каждого рыцаря
    атрибуты:
        __ENEMY - количество врагов
        __lock - блокировка выполнения задачи потоком. Из-за гонки потоков
            print не успевает выводить перенос строк.
    методы:
        __init__
            инициализация и проверка на соответствие параметров
            условиям задачи
        run
            описание битвы
        sklonenie
            принимает параметр - число
            реализовывает вывод информации по падежам в зависимости от числа,
            после 20 выводит общую информацию 'день(дня)'
    '''
    __ENEMY = 100
    __lock = threading.Lock()

    def __init__(self,name, power):
        threading.Thread.__init__(self)
        if isinstance(name,str):
            self.name = name
        else:
            self.name = Noname_knight

        if isinstance(power,int):
            self.power = power
        else:
            self.power = 1
    def sklonenie(self,v):
        if v == 1:
            return 'день'
        elif v >=2 and v < 5:
            return 'дня'
        elif v >= 5 and v <=20:
            return 'дней'
        else:
            return 'день(дня)'

    def run(self):
        print(f'{self.name} на нас напали!')
        day = 0
        while self.__ENEMY > 0:
            time.sleep(1)
            day += 1
            self.__ENEMY -= self.power
            self.__lock.acquire() # Блокируем вывод информации для другого потока
            print(f'{self.name} сражается {day} {self.sklonenie(day)}..., осталось {self.__ENEMY} воинов.')
            self.__lock.release() # Снимаем блокировку для другого потока

        print(f'{self.name} одержал победу спустя {day} дней(дня)!')


first_knight = knight('Sir Lancelot', 10)
second_knight = knight('Sir Galahad',20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')