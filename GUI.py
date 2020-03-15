from tkinter import Tk, Label, Button
from tkinter.filedialog import askopenfilename

from record import Record_Thread
from replay import replay
from threading import Thread

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="Press F12 to Start Recording\nPress Again to Stop\n")
        self.label.pack()

        self.record_button = Button(master, text="Start Recording", command=self.start_recording)
        self.record_button.pack()

        self.replay_button = Button(master, text="Start Replaying", command=self.start_replaying)
        self.replay_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        # start recording function
        # record_controller()

    def start_recording(self):
        # print("start_recording!")
        self.master.withdraw()

        # start the 
        t = Record_Thread(self.master)
        record_thread = Thread(target=t.run())
        record_thread.start()


    def start_replaying(self):
        self.master.withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        print(filename)
        # start replaying 
        replay(filename)

        self.master.deiconify()


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
