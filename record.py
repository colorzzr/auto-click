import pynput.mouse as mouses
import pynput.keyboard as keyboard
import json
import datetime


class record_controller(object):
    """docstring for record_controller"""
    def __init__(self):
        super(record_controller, self).__init__()
        self.start = False
        self.file = open("record_%s.txt"%(datetime.datetime.now()), 'w')

    def on_press(self, key):
        # start recording if f12 is first pressed
        # stop listen if f12 is second pressed
        if key == keyboard.Key.f12:
            self.start = not self.start
            if self.start:
                print("###### Start recording")
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

# print("on")
# with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
# with mouses.Listener(on_click=on_click) as listener:
#     try:
#         listener.join()
#     except Exception as e:
#         print('Done'.format(e.args[0]))