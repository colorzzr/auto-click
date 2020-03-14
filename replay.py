import pynput.mouse as mouses
import pynput.keyboard as keyboards
import json
import time


def replay():
    file = open('record_2020-02-02 12:55:23.809343.txt', 'r')
    lines = file.readlines()

    mouse = mouses.Controller()
    # mapping table for string to object value
    mouse_button_mapping = {
        'Button.left': mouses.Button.left,
        'Button.right': mouses.Button.right,
    }
    keyboard = keyboards.Controller()


    for x in lines:
        log = json.loads(x)
        event = log['event_type']

        # base on action to take action
        if event == 'mouse_click':
            action = log['extra']

            # for eact click I have position and button 
            mouse.position = (action['x_pos'], action['y_pos'])
            # simulat click
            button = mouse_button_mapping[action['button']]
            mouse.click(button, 1)

        elif event == 'button_click':
            action = log['extra']

            # # simulate the keyboard press
            button = action['button'][1:-1]
            keyboard.touch(button, True)


        # print(log['event_type'])

        # sleep 0.5 second in case I click too fast
        time.sleep(0.5)