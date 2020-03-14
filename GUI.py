from tkinter import Tk, Label, Button
from record import Record_Thread
from threading import Thread

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="Press F12 to Start Recording\nPress Again to Stop\n")
        self.label.pack()

        self.greet_button = Button(master, text="Start Recording", command=self.start_recording)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        # start recording function
        # record_controller()

    def start_recording(self):
        # print("start_recording!")
        self.master.withdraw()
        
        # start the 
        print(self.master)
        t = Record_Thread(self.master)
        record_thread = Thread(target=t.run())
        record_thread.start()

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
