import sys
import getpass
from examdownloader import examdownloader, openFile

module = 'CS1010S'
username = 'E0123456'
destination = './'

def startDownload(args):

    global module, username
    password = ''

    if len(args) > 0:
        module = args[0]
        username = args[1]

    password = getpass.getpass('Enter password for ' + username + ': ')
    ed = examdownloader('CLI')


    def updateStatus(msg, type='normal'):
        print msg

    def downloadCallback(status, lastfile='', numFiles=0):
        if status:
            updateStatus(str(numFiles) + ' papers downloaded successfully!', 'success')
            openFile(lastfile)
        else:
            updateStatus('Paper not released by Department', 'error')

    ed.getContents(module, username, password, destination, downloadCallback, updateStatus)

if __name__ == '__main__':
    startDownload(sys.argv[1:])
