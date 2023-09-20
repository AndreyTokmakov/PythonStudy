import multiprocessing
import os
import subprocess
import sys
import time


def print_mynumber(count: int):
    for i in range(0, count):
        print("print_mynumber: ", i)
        time.sleep(0.25)


def create_process():
    # Process with run print_mynumber() function with parameter count = 1 as the separate process
    sub_process = multiprocessing.Process(target=print_mynumber, args=(10,))

    # start the process
    sub_process.start()

    # Wait for process to finish
    sub_process.join()


def open_notepad_wait_and_close_1():
    proc = subprocess.Popen(["notepad.exe"])
    time.sleep(5)


def open_notepad_wait_and_close_2():
    os.system("notepad.exe")
    time.sleep(5)


if __name__ == '__main__':
    create_process()

    # open_notepad_wait_and_close_2()

    # open_notepad_wait_and_close_1()

