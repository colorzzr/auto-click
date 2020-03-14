import pynput.mouse as mouses
import pynput.keyboard as keyboard
import json

from threading import Thread, Event
from datetime import datetime, timedelta
import time
import json

class record_controller(object):
    """docstring for record_controller"""
    def __init__(self):
        super(record_controller, self).__init__()
        self.start = True
        self.file = open("./record_%s.txt"%(datetime.now()), 'w')



    def on_press(self, key):
        # start recording if f12 is first pressed
        # stop listen if f12 is second pressed
        if key == keyboard.Key.f12:
            self.start = not self.start
            if self.start:
                print("###### Start recording")
                self.file = open("./record_%s.txt"%(datetime.now()), 'w')
            else:
                print("###### Stop recording")
                self.file.close()
                return False

        # if flag is true we start put into logs
        elif self.start:
            log = {
                'event_type':'button_click',
                'extra':{
                    'button': '%s'%key,
                }
            }
            self.file.write('%s\n'%json.dumps(log))


    def on_click(self, x, y, button, pressed):
        # print(button)
        # if flag is true we start put into logs
        if pressed and self.start:
            log = {
                'event_type':'mouse_click',
                'extra':{
                    'button': '%s'%button,
                    'x_pos': x,
                    'y_pos': y
                }
            }
            self.file.write('%s\n'%json.dumps(log))


class Record_Thread(Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, master_window):
        print("###### __init__")
        super(Record_Thread, self).__init__()
        self._stop_event = Event()
        # the UI windoe
        self.master = master_window


    def run(self):
        print("###### run")
        c = record_controller()
        key_listener = keyboard.Listener(on_press=c.on_press)
        # key_listener.start()

        ########################################################## Mouse ########################################################
        mouse_listener = mouses.Listener(on_click=c.on_click)
        mouse_listener.start()


        with key_listener as listener:
            try:
                listener.join()
            except Exception as e:
                print(e)
                print('Done'.format(e.args[0]))

        self.master.deiconify()
        print("# DONE")



    def stop(self):
        self._stop_event.set()
        # decrease the connection
        # self.connection_count -= 1

    def stopped(self):
        return self._stop_event.is_set()