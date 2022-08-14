from tkinter import *
from tkinter import filedialog as tkFileDialog
import subprocess
import _thread
import examdownloader

FONT = ('Arial', 14, 'bold')

class examdownloadergui(object):
    def __init__(self):
        self.module = ''
        self.username = ''
        self.password = ''
        self.destination = ''

        root = Tk()
        root.withdraw()
        root.update_idletasks()  # Update "requested size" from geometry manager

        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
        root.geometry("+%d+%d" % (x, y))
        root.deiconify()

        root.title('NUS Past Year Exam Paper Downloader')
        root.resizable(0, 0)

        self.top = Frame(root)
        self.top.grid(row=0, column=0, padx=20, pady=20)
        self.top.columnconfigure(0, weight=1)
        self.top.rowconfigure(0, weight=1)

        titleLabel = Label(self.top, text='NUS PYP Downloader', font=('Arial', 28, 'bold'))
        titleLabel.grid(row=1, column=0, columnspan=3, padx=20, pady=20)

        moduleLabel = Label(self.top, text='Module Code:', font=FONT)
        moduleLabel.grid(row=2, column=0)
        self.moduleField = Entry(self.top, bd=2, textvariable=self.module)
        self.moduleField.grid(row=2, column=1)
        empty = Label(self.top, text='')
        empty.grid(row=2, column=2, rowspan=3)

        usernameLabel = Label(self.top, text='NUSNET ID:', font=FONT)
        usernameLabel.grid(row=3, column=0)
        self.usernameField = Entry(self.top, bd=2, textvariable=self.username)
        self.usernameField.insert(0, self.username)
        self.usernameField.grid(row=3, column=1)

        passwordLabel = Label(self.top, text='Password:', font=FONT)
        passwordLabel.grid(row=4, column=0)
        self.passwordField = Entry(self.top, bd=2, show='*', textvariable=self.password)
        self.passwordField.insert(0, self.password)
        self.passwordField.grid(row=4, column=1)

        destLabel = Label(self.top, text='Save To Destination:', font=FONT)
        destLabel.grid(row=5, column=0)
        self.destField = Entry(self.top, bd=2, textvariable=self.destination)
        self.destField.insert(0, self.destination)
        self.destField.grid(row=5, column=1)
        destButton = Button(self.top, text='Choose Folder', command=self.askForDestination)
        destButton.grid(row=5, column=2)

        self.statusLabel = Label(self.top, text='Brought to you by Oh Shunhao and NUSMods')
        self.statusLabel.grid(row=6, columnspan=3, padx=20, pady=20)

        startButton = Button(self.top, text='Start Download!', command=self.startDownload)
        startButton.grid(row=7, columnspan=3)

        root.mainloop()

    def askForDestination(self):
        self.destination = tkFileDialog.askdirectory(mustexist=False, parent=self.top, title='Choose a destination')
        self.destField.delete(0, END)
        self.destField.insert(0, self.destination)

    def startDownload(self):
        module = self.moduleField.get()
        username = self.usernameField.get()
        password = self.passwordField.get()
        base_destination = self.destField.get()
        ed = examdownloader.examdownloader('GUI')

        def downloadCallback(status, lastfile='', numFiles=0):
            if status:
                self.updateStatus(str(numFiles) + ' papers downloaded successfully!', 'success')
#                subprocess.call(['open', '-R', lastfile])
            else:
                self.updateStatus('Paper not released by Department', 'error')

        for mod in module.split(','):
            mod = mod.strip()
            destination = f"{base_destination}/{mod}/Past Year Papers"
            _thread.start_new_thread(ed.getContents, (mod, username, password, destination, downloadCallback, self.updateStatus))

    def updateStatus(self, msg, type='normal'):
        self.statusLabel['text'] = msg
        if type == 'success':
            self.statusLabel['fg'] = 'green'
        elif type == 'error':
            self.statusLabel['fg'] = 'red'
        else:
            self.statusLabel['fg'] = 'blue'

if __name__ == '__main__':
    examdownloadergui()
