from inputimeout import inputimeout, TimeoutOccurred
try:
    something = inputimeout(prompt='>>', timeout=5)
except TimeoutOccurred:
    something = 'something'
print(something)

import ctypes  # An included library with Python install.
mbox_value=ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 0)
print(mbox_value)


from tkinter import *

WELCOME_MSG = '''Welcome to this event.

Your attendance has been registered.

Don't forget your free lunch.'''
WELCOME_DURATION = 2000

def welcome():
    top = Toplevel()
    top.title('Welcome')
    Message(top, text=WELCOME_MSG, padx=20, pady=20).pack()
    top.after(WELCOME_DURATION, top.destroy)

root = Tk()
#Button(root, text="Click to register", command=welcome).pack()
welcome()
root.mainloop()



from tkinter import Tk
from tkinter.messagebox import Message
from _tkinter import TclError

TIME_TO_WAIT = 2000 # in milliseconds
root = Tk()
root.withdraw()
try:
    root.after(TIME_TO_WAIT, root.destroy)
    Message(title="your title", message="your message", master=root).show()
except TclError:
    pass

import pymsgbox
msg_val=pymsgbox.confirm('Nuke the site from orbit?', 'Confirm nuke', ["Yes, I'm sure.", 'Cancel'], timeout=2000)  # closes after 2000 milliseconds (2 seconds)
print(msg_val)


#%%


from threading import Thread
class MTThread(Thread):
    def __init__(self, name = "", target = None,args = None):
        self.mt_name = name
        self.mt_target = target
        self.args = args
        Thread.__init__(self, name = name, target = target)
    def start(self):
        super().start()
        Thread.__init__(self, name = self.mt_name, target = self.mt_target,args=self.args)
    def run(self):
        super().run()
        Thread.__init__(self, name = self.mt_name, target = self.mt_target, args=self.args)
def code():
    global play_sound_boolean
    names="\n".join(names)
    print(names)
    msg_val = pymsgbox.alert('Vaccine Available!!!'+names, 'Vaccine Available!!!',timeout=2000)  # closes after 2000 milliseconds (2 seconds)
    #print(msg_val)
    play_sound_boolean =True if msg_val!= 'Timeout' else False
    #print(acknowledge)

    return play_sound_boolean
thread = MTThread(target=get_play_sound_boolean,args=response_df_available.name)
thread.start()
thread.start()
#%%
from threading import Thread
@ThreadKiller(arg) #qu'est-ce que c'est
def RefreshThreads():
    threadTask1 = threading.Thread(name = "Task1", target = play_sound, args = (anyArguments))
    threadTask2 = threading.Thread(name = "Task2", target = play_sound, args = (anyArguments))
    threadTask1.start()
    threadTask2.start()

#Main
while True:
    #do stuff
    threadRefreshThreads = threading.Thread(name = "RefreshThreads", target = RefreshThreads, args = ())
    threadRefreshThreads.start()
#%%
from pytictoc import TicToc
t = TicToc() # create TicToc instance
t.tic() # Start timer
play_sound()
t.toc() # Print elapsed time
#%%
df=pd.read_csv()