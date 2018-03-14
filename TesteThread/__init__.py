# Projeto: VemPython/__init__.py
# Autor: rafael
# Data: 14/03/18 - 10:03
# Objetivo: TODO teste de funcionalidade de uma Thread em Python

from threading import Thread
import sys

COUNTDOWN = 5

class Th(Thread):

    def __init__ (self, num):
        sys.stdout.write("\nMaking thread number " + str(num) + "n")
        sys.stdout.flush()
        Thread.__init__(self)
        self.num = num
        self.countdown = COUNTDOWN

    def run(self):

        while (self.countdown):
            sys.stdout.write("\nThread " + str(self.num) +
                             " (" + str(self.countdown) + ")n")
            sys.stdout.flush()
            self.countdown -= 1


for thread_number in range (5):
    thread = Th(thread_number)
    thread.start()