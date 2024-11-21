# Банковские операции
from random import randint
from time import sleep
import threading


class Bank:
    '''Класс выполняет операции по увеличению и уменьшению баланса на счете
    атрибуты
        __LOCK
            этот атрибут обеспечивает блокировку параллельных процессов
        balance
            этот атрибут является представлением расчетного счета для
            операций над средствами
        transaction
            этот атрибут отвечает за количество операций со счетом
            (введен для гибкости программы)
        min_quant
            атрибут содержит минимальное значение суммы операции
            (введен для гибкости программы)
        max_quant
            атрибут содержит максимальное значение суммы операции
            (введен для гибкости программы)
    методы
        __init__
            метод устанавливает количество транзакций, а так же минимальное и максимальное значение
            суммы операции
        sklonenie
            метод возвращяет название валюты в соответствии с падежом
        deposit
            метод осуществляет пополнение счета
        take
            метод осуществляет снятие со счета, осуществляется проверка достаточности средств на балансе
        '''
    __LOCK = threading.Lock()
    balance = 0

    def __init__(self):
        self.transaction = 10
        self.min_quant = 50
        self.max_quant = 500

    def sklonenie(self, v):
        if v == 1:
            return 'рубль'
        elif v >= 2 and v < 5:
            return 'рубля'
        elif v >= 5 and v <= 20:
            return 'рублей'
        elif v > 20:
            o = v % 10
            if o == 1:
                return 'рубль'
            if o >= 2 and o < 5:
                return 'рубля'
            elif o >= 5 or o == 0:
                return 'рублей'
            else:
                return 'p.'

    def deposit(self):
        for i in range(self.transaction):
            quant = randint(self.min_quant, self.max_quant)
            self.balance += quant
            print(f'Пополнение: {quant} {self.sklonenie(quant)}. Баланс: {self.balance} {self.sklonenie(self.balance)}')
            if self.balance >= 500 and self.__LOCK.locked():
                self.__LOCK.release()
            sleep(0.001)

    def take(self):
        for i in range(self.transaction):
            quant = randint(self.min_quant, self.max_quant)
            print(f'Запрос на снятие: {quant} {self.sklonenie(quant)}')
            if quant <= self.balance:
                self.balance -= quant
                print(f'Снятие: {quant} {self.sklonenie(quant)}. Баланс: {self.balance} {self.sklonenie(self.balance)}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.__LOCK.acquire()


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
