from multiprocessing import Queue
from multiprocessing.context import Process

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from pincode import PinCode
from multithreader import process_manager
import sys


def main():
    pin_slot = PinCode()
    q = Queue()
    # Process(target=process_manager, args=(pin_slot.day, q, 686575, "11-05-2021", 18)).start()
    Process(target=process_manager, args=(pin_slot.week, q, 744302, "11-05-2021", 45)).start()
    while True:
        response = q.get()
        print(response)

    # Process(target=process_manager, args=(pin_slot.day, 744302, "03-05-2021")).start()
    # pin_slot.week(pin=744302, search_date="03-05-2021")
    # print(pin_slot.day(pin=744302, search_date="03-05-2021"))


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("Vaccine slot finder")

    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    # main()
    window()
