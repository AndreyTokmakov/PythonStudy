import time
import datetime


def print_time():
    print(datetime.datetime.now())

    local_time = time.localtime()
    a = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    print(a)


def sleep_test():
    print(datetime.datetime.now())

    time.sleep(2)

    print(datetime.datetime.now())


if __name__ == '__main__':
    # print_time()
    sleep_test()
