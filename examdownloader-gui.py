import examdownloader
from Tkinter import *
import tkFileDialog

class examdownloadergui(object):
    def __init__(self):
        self.module = ''
        self.username = ''
        self.password = ''
        self.destination = ''

        root = Tk()
        root.title('NUS Past Year Exam Paper Downloader')

        self.top = Frame(root)
        self.top.grid(row=0, column=0, padx=20, pady=20)
        self.top.columnconfigure(0, weight=1)
        self.top.rowconfigure(0, weight=1)

        moduleLabel = Label(self.top, text='Module Code:')
        moduleLabel.grid(row=1, column=0)
        self.moduleField = Entry(self.top, bd=2, textvariable=self.module)
        self.moduleField.grid(row=1, column=1, columnspan=2)

        usernameLabel = Label(self.top, text='NUSNET ID:')
        usernameLabel.grid(row=2, column=0)
        self.usernameField = Entry(self.top, bd=2, textvariable=self.username)
        self.usernameField.grid(row=2, column=1, columnspan=2)

        passwordLabel = Label(self.top, text='Password:')
        passwordLabel.grid(row=3, column=0)
        self.passwordField = Entry(self.top, bd=2, show='*', textvariable=self.password)
        self.passwordField.grid(row=3, column=1, columnspan=2)

        destLabel = Label(self.top, text='Destination:')
        destLabel.grid(row=4, column=0)
        self.destField = Entry(self.top, bd=2, textvariable=self.destination)
        self.destField.grid(row=4, column=1)
        destButton = Button(self.top, text="...", command=self.askForDestination)
        destButton.grid(row=4, column=2)

        self.statusLabel = Label(self.top, text='^____^', justify=CENTER)
        self.statusLabel.grid(row=5, columnspan=3)

        startButton = Button(self.top, text='Start!', command=self.startDownload)
        startButton.grid(row=6, columnspan=3)

        root.mainloop()

    def askForDestination(self): 
        self.destination = tkFileDialog.askdirectory(mustexist=False, parent=self.top, title='Choose a destination')
        self.destField.delete(0)
        self.destField.insert(0, self.destination)

    def startDownload(self):
        module = self.moduleField.get()
        username = self.usernameField.get()
        password = self.passwordField.get()
        destination = self.destField.get()
        ed = examdownloader.examdownloader('GUI')

        def downloadCallback(result):
            if result:
                self.updateStatus('Done!', 'success')
            else:
                self.updateStatus('Failed!', 'error')

        ed.getContents(module, username, password, destination, downloadCallback)

    def updateStatus(self, msg, type='normal'): 
        self.statusLabel['text'] = msg
        if type == 'success':
            self.statusLabel['fg'] = 'green'
        elif type == 'error':
            self.statusLabel['fg'] = 'red'

if __name__ == '__main__':
    examdownloadergui()
