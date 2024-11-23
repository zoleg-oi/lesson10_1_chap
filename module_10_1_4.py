# Очереди для обмена данными между потоками.
# Потоки гостей в кафе
import threading
from queue import Queue
from random import randint
from time import sleep


class Table:
    '''
    Данный класс образует стол в кафе
    получает параметр - номер стола в формате int
    имеет атрибуты:
    number
        номер стола, если получаем неправильный параметр, то считаем, что номер стола - 0
    guest
        объект гость, при создании экземпляра класса получает значение - None
    '''

    def __init__(self, num):

        if isinstance(num, int):
            self.number = num
        else:
            self.number = 0
        self.guest = None


class Guest(threading.Thread):
    '''
    Данный класс создает посетителя кафе
    является потомком класса threding
    имеет атрибуты:
    name - имя пользователя
    методы
    run
        это время еды, выбранное случайным образом от 3 до 10 с.
        выполняется путем оформления задержки.
    '''

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    '''
    Данный класс имитирует работу кафе
    имеет атрибуты
    __QUEUE
        Очередь из посетителей, которые не смогли разместиться в кафе
    tables
        Количество столов в кафе
    Методы:
    empty_table
        Метод не задействован, показан для примера.
        Определяет номер пустого стола
    guest_arrival
        метод имитирует открытие кафе и рассаживает посетителей за свободные столы,
        тех кто не поместился, ставит в очередь
    discuss_guests
        метод имитирует обслуживание клиентов
        если стол освободился, то сажает посетителя за свободный столик.
        и так до тех пор, пока очередь не закончится.
    '''
    __QUEUE = Queue()

    def __init__(self, *tables):
        self.tables = tables

    # Дополнительный метод для определения свободного стола.
    # как один из вариантов решения
    def empty_table(self):
        for i in self.tables:
            if i.guest is None:
                return i.number
        return 0

    def guest_arrival(self, *guests):
        for i in guests:
            # номер свободного стола можно определить и таким образом
            #            nt = self.empty_table()
            #            if nt > 0:
            #                self.tables[nt - 1].guest = i
            #                self.tables[nt - 1].guest.start()
            #                print(f'{i.name} сел(-а) за стол номер {nt}')
            #            else:
            #                self.__queue.put(i)
            #                print(f'{i.name} в очереди".')

            sit_down = False  # Это семафор, который сообщает о свободных столах
            for ii in self.tables:
                if ii.guest is None:
                    ii.guest = i
                    ii.guest.start()
                    print(f'{i.name} сел(-а) за стол номер {ii.number}')
                    sit_down = True  # Стол свободен и был занят
                    break
            if sit_down == False:  # свободные столы закончились остальных помещаем в очередь
                self.__QUEUE.put(i)
                print(f'{i.name} в очереди".')

    def discuss_guests(self):
        while True:
            for i in self.tables:
                if i.guest == None:
                    if not self.__QUEUE.empty():  # Если очередь не пустая, то сажаем за стол следующего
                        i.guest = self.__QUEUE.get()
                        i.guest.start()
                        print(f'{i.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {i.number}')
                else:
                    if i.guest.is_alive() == False:
                        print(f'{i.guest.name} за {i.number} столом > покушал(-а) и ушёл(ушла) \n '
                              f'Стол с номером {i.number} Свободен')
                        i.guest = None
            # Очередь закончилась и все столы свободны, процессы еды закончены
            if self.__QUEUE.empty() and threading.active_count() == 1:
                break


tables = [Table(number) for number in range(1, 6)]
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
