# Многопроцессное считывание
import time
from multiprocessing import Pool
import os.path


def read_info(*name_file):
    all_data = []
    for f in name_file:
        if os.path.exists(f):
            file = open(f, 'r')
            lines = file.readlines()
            for line in lines:
                all_data.append(line)
                if not line:
                    file.close()
                    break
            print(f)
        else:
            print(f'файл: {f} не найден')


filenames = [f'file {number}.txt' for number in range(1, 5)]

# start = time.time()
# ri = read_info(*filenames)
# finish = time.time()
# print(f'Время работы программы - {str(finish - start)}')


if __name__ == "__main__":
    with Pool() as pool:
        start = time.time()
        res = pool.map(read_info, filenames)
        finish = time.time()
        print(f'Время работы программы - {str(finish - start)}')
